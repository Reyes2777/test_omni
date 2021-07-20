import os

from tortoise import Tortoise


async def run(generate_schemas=False):
    await Tortoise.init(
        config={
            'connections': {
                'omni': {
                    'engine': 'tortoise.backends.asyncpg',
                    'credentials': {
                        'host': os.environ['DB_HOST'],
                        'port': os.environ['DB_PORT'],
                        'user': os.environ['DB_USER'],
                        'password': os.environ['DB_PASSWORD'],
                        'database': os.environ['DB_NAME'],
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
