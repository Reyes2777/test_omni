from starlette.applications import Starlette

from omni import response
from omni.controllers.product import ProductController

product_api = Starlette()


@product_api.route(path='/create/', methods=('POST',))
async def create(request):
    data = await request.json()
    product_controller = ProductController()
    product, message = await product_controller.create(**data)
    if product:
        return response(message=message, status_code=200)
    return response(message=message, status_code=400)


@product_api.route(path='/get/{product_id:int}', methods=('GET',))
async def get(request):
    product_id = request.path_params['product_id']
    product = await ProductController.get(id=product_id)
    data = product.to_dict()
    if product:
        return response(message='product found', data=data, status_code=200)
    return response(message='product not found', status_code=400)


@product_api.route(path='/delete/{product_id:int}', methods=('GET',))
async def delete(request):
    product_id = request.path_params['product_id']
    product = await ProductController.get(id=product_id)
    if product:
        await ProductController().delete(_id=product_id)
        return response(message='product delete', status_code=200)
    return response(message='product don`t exist', status_code=400)


@product_api.route(path='/update/{product_id:int}', methods=('POST',))
async def update(request):
    product_id = request.path_params['product_id']
    data = await request.json()
    product = await ProductController.get(id=product_id)
    if product:
        product = await ProductController().update(_id=product_id, **data)
        if product:
            data = product.to_dict()
            return response(message='product update', data=data, status_code=200)
        return response(message='product not update', status_code=400)
    return response(message='product don`t exist', status_code=400)


@product_api.route(path='/all/', methods=('GET',))
async def all(request):
    all_products = await ProductController.all()
    list_products = []
    for product in all_products:
        list_products.append(product.to_dict())
    return response(message='All products', data=list_products, status_code=200)
