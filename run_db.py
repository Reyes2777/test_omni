import os

from tortoise import Tortoise


async def run(generate_schemas=False):
    await Tortoise.init(
        config={
            'connections': {
                'omni': {
                    'engine': 'tortoise.backends.asyncpg',
                    'credentials': {
                        'host': os.environ['DEFAULT_DB_HOST'],
                        'port': os.environ['DEFAULT_DB_HOST_PORT'],
                        'user': os.environ['DEFAULT_DB_USER'],
                        'password': os.environ['DEFAULT_DB_PASSWORD'],
                        'database': os.environ['DEFAULT_DB_NAME'],
                    }
                }
            },
            'apps': {
                'omni': {
                    'models': ['omni.models'],
                    'default_connection': 'omni'
                }
            }
        }
    )
    if generate_schemas:
        await Tortoise.generate_schemas()
