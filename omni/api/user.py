from starlette.applications import Starlette

from omni import response
from omni.controllers.user import UserController
from omni.models import User

user_api = Starlette()


@user_api.route(path='/create/', methods=('POST',))
async def create(request):
    data = await request.json()
    user_controller = UserController()
    user, message = await user_controller.create(**data)
    if user:
        return response(message=message, status_code=200)
    return response(message=message, status_code=400)
