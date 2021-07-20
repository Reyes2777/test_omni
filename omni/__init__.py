from starlette.applications import Starlette
from starlette.routing import Route

from DB import run
from omni.utils import response


async def homepage(request):
    return response(message='Successfully', status_code=200)

app = Starlette(debug=True, routes=[Route('/', homepage)])
from omni.api import user_api
app.mount('/api/user', user_api)


@app.on_event('startup')
async def init_db():
    await run(generate_schemas=True)
