from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

from run_db import run


async def homepage(request):
    return JSONResponse({'hello': 'world'})

app = Starlette(debug=True, routes=[Route('/', homepage)])


@app.on_event('startup')
async def init_db():
    await run()
