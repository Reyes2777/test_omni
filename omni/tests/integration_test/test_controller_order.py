from pytest import mark

from omni.controllers.order import OrderController


@mark.parametrize('data', (
        (
                {"name": "Balloon", "value": 10000, 'response': 'Successfully created Order'},
                {"name": "Toy Car", "value": 12000, 'response': 'Successfully created Order'},
         )))
@mark.asyncio
async def test_create_order(db_transaction, data, user_fixture, product_fixture):
    data['user'] = user_fixture
    data['products_id'] = [product_fixture.id]
    message_expected = data.pop('response')
    order_controller = OrderController()
    order, message = await order_controller.create(**data)
    assert message_expected == message


@mark.asyncio
async def test_get_order( db_transaction, user_fixture, product_fixture):
    data = {
        'user': user_fixture,
        'products_id': [product_fixture.id]
    }
    order_controller = OrderController()
    order, message = await order_controller.create(**data)
    order = await OrderController.get(id=order.id)
    assert order


@mark.asyncio
async def test_get_user_none(db_transaction):
    order = await OrderController.get(id=0)
    assert order is None


@mark.asyncio
async def test_update_order(db_transaction, user_fixture, product_fixture):
    data = {
        'user': user_fixture,
        'products_id': [product_fixture.id]
    }
    order_controller = OrderController()
    order, message = await order_controller.create(**data)
    data.pop('products_id')
    order = await OrderController().update(_id=order.id, **data)
    assert order


@mark.asyncio
async def test_delete(db_transaction, user_fixture, product_fixture):
    data = {
        'user': user_fixture,
        'products_id': [product_fixture.id]
    }
    order_controller = OrderController()
    order, message = await order_controller.create(**data)
    await OrderController().delete(_id=order.id)
    order = await OrderController.get(id=order.id)
    assert order is None
