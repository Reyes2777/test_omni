import asyncio
import logging
import os
import subprocess

import asyncpg
from _pytest.fixtures import fixture

from DB import run

logger = logging.getLogger('OMNI')


@fixture(scope='session')
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@fixture(scope='session')
async def create_db():
    subprocess.call(['psql', '-U', os.environ['DB_USER'], '-w', '-h', os.environ['DB_HOST'], '-p', os.environ['DB_PORT'], '-d',
                     os.environ['DB_NAME'],'-f', f'{os.path.dirname(__file__)}/db.sql'])
    os.environ['DB_NAME'] = os.environ['DB_NAME'] + '_test'
    await run(generate_schemas=True)


@fixture
def db_connection(create_db, event_loop):
    connection = event_loop.run_until_complete(asyncpg.connect(
        host=os.environ['DEFAULT_DB_HOST'],
        database=os.environ['DEFAULT_DB_NAME'],
        password=os.environ['DEFAULT_DB_PASSWORD'],
        port=os.environ['DEFAULT_DB_HOST_PORT'],
        user=os.environ['DEFAULT_DB_USER'],
        timeout=5
    ))
    yield connection
    event_loop.run_until_complete(connection.close())


@fixture
def db_transaction(event_loop, db_connection):
    yield
    logger.debug('Doing rollback...')
    event_loop.run_until_complete(db_connection.execute(
        'TRUNCATE public.user, public.order, public.product, public.shipment, public.payment CASCADE;'
    ))
