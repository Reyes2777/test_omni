from starlette.applications import Starlette

from omni import response
from omni.controllers.order import orderController

order_api = Starlette()


@order_api.route(path='/create/', methods=('POST',))
async def create(request):
    data = await request.json()
    order_controller = orderController()
    order, message = await order_controller.create(**data)
    if order:
        return response(message=message, status_code=200)
    return response(message=message, status_code=400)


@order_api.route(path='/get/{order_id:int}', methods=('GET',))
async def get(request):
    order_id = request.path_params['order_id']
    order = await orderController.get(id=order_id)
    data = order.to_dict()
    if order:
        return response(message='order found', data=data, status_code=200)
    return response(message='order not found', status_code=400)


@order_api.route(path='/delete/{order_id:int}', methods=('GET',))
async def delete(request):
    order_id = request.path_params['order_id']
    order = await orderController.get(id=order_id)
    if order:
        await orderController().delete(_id=order_id)
        return response(message='order delete', status_code=200)
    return response(message='order don`t exist', status_code=400)


@order_api.route(path='/update/{order_id:int}', methods=('POST',))
async def update(request):
    order_id = request.path_params['order_id']
    data = await request.json()
    order = await orderController.get(id=order_id)
    if order:
        order = await orderController().update(_id=order_id, **data)
        if order:
            data = order.to_dict()
            return response(message='order update', data=data, status_code=200)
        return response(message='order not update', status_code=400)
    return response(message='order don`t exist', status_code=400)


@order_api.route(path='/all/', methods=('GET',))
async def all(request):
    all_orders = await orderController.all()
    list_orders = []
    for order in all_orders:
        list_orders.append(order.to_dict())
    return response(message='All orders', data=list_orders, status_code=200)
