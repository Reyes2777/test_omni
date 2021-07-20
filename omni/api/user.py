from starlette.applications import Starlette

from omni import response
from omni.controllers.user import UserController

user_api = Starlette()


@user_api.route(path='/create/', methods=('POST',))
async def create(request):
    data = await request.json()
    user_controller = UserController()
    user, message = await user_controller.create(**data)
    if user:
        return response(message=message, status_code=200)
    return response(message=message, status_code=400)


@user_api.route(path='/get/{user_id:int}', methods=('GET',))
async def get(request):
    user_id = request.path_params['user_id']
    user = await UserController.get(id=user_id)
    data = user.to_dict()
    if user:
        return response(message='User found', data=data, status_code=200)
    return response(message='User not found', status_code=400)


@user_api.route(path='/delete/{user_id:int}', methods=('GET',))
async def delete(request):
    user_id = request.path_params['user_id']
    user = await UserController.get(id=user_id)
    if user:
        await UserController().delete(_id=user_id)
        return response(message='User delete', status_code=200)
    return response(message='User don`t exist', status_code=400)


@user_api.route(path='/update/{user_id:int}', methods=('POST',))
async def update(request):
    user_id = request.path_params['user_id']
    data = await request.json()
    user = await UserController.get(id=user_id)
    if user:
        user = await UserController().update(_id=user_id, **data)
        if user:
            data = user.to_dict()
            return response(message='User update', data=data, status_code=200)
        return response(message='User not update', status_code=400)
    return response(message='User don`t exist', status_code=400)


@user_api.route(path='/all/', methods=('GET',))
async def all(request):
    all_users = await UserController.all()
    list_users = []
    for user in all_users:
        list_users.append(user.to_dict())
    return response(message='All Users', data=list_users, status_code=200)
