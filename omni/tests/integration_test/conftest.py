import asyncio
import os
import subprocess

import asyncpg
from _pytest.fixtures import fixture
from starlette.testclient import TestClient

from DB import run
from omni import app
from omni.tests.integration_test.factories import UserFactory, ProductFactory


@fixture(scope='session')
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@fixture(scope='session')
async def create_db():
    print(f'Creating DB_TEST with user {os.environ["DB_USER"]}.......')
    subprocess.call(['psql', '-U', os.environ['DB_USER'], '-w', '-h', os.environ['DB_HOST'], '-p', os.environ['DB_PORT'], '-d',
                     os.environ['DB_NAME'], '-f', f'{os.path.dirname(__file__)}/db.sql'])
    os.environ['DB_NAME'] = os.environ['DB_NAME'] + '_test'
    print('Generating schemas....')
    await run(generate_schemas=True)


@fixture
def db_connection(create_db, event_loop):
    print(f'Creating DB CONNECTION with {os.environ["DB_NAME"]}')
    connection = event_loop.run_until_complete(asyncpg.connect(
        host=os.environ['DB_HOST'],
        database=os.environ['DB_NAME'],
        password=os.environ['DB_PASSWORD'],
        port=os.environ['DB_PORT'],
        user=os.environ['DB_USER'],
        timeout=5
    ))
    yield connection
    event_loop.run_until_complete(connection.close())


@fixture
def db_transaction(event_loop, db_connection):
    yield
    print('Doing rollback...')
    event_loop.run_until_complete(db_connection.execute(
        'TRUNCATE public.user, public.order, public.product, public.shipment, public.payment CASCADE;'
    ))


@fixture
def api_client_fixture():
    return TestClient(app=app)


@fixture
async def user_fixture():
    user = UserFactory.build()
    await user.save()
    return user


@fixture
async def product_fixture():
    product = ProductFactory.build()
    await product.save()
    return product