from pytest import mark

from omni.controllers.product import ProductController
from omni.controllers.user import UserController


@mark.parametrize('data', (
        (
                {"name": "Balloon", "value": 10000, 'response': 'Successfully created Product'},
                {"name": "Toy Car", "value": 12000, 'response': 'Successfully created Product'},
         )))
@mark.asyncio
async def test_create_product(db_transaction, data):
    message_expected = data.pop('response')
    product_controller = ProductController()
    product, message = await product_controller.create(**data)
    assert message_expected == message


@mark.asyncio
async def test_create_product_without_value(db_transaction):
    data = {
        "name": "Ballon"
    }
    product_controller = ProductController()
    product, message = await product_controller.create(**data)
    assert product is None
    assert 'Error Product' in message


@mark.asyncio
async def test_get_product(db_transaction, product_fixture):
    product = await ProductController.get(id=product_fixture.id)
    assert product.name == 'Ballon'
    assert product.value == 10000


@mark.asyncio
async def test_get_user_none(db_transaction):
    product = await ProductController.get(id=0)
    assert product is None


@mark.asyncio
async def test_update_user(db_transaction, product_fixture):
    data = {
        "name": "Ballon 2",
        "value": 12000
    }
    product = await ProductController().update(_id=product_fixture.id, **data)
    assert product.name == 'Ballon 2'
    assert product.value == 12000


@mark.asyncio
async def test_delete(db_transaction, product_fixture):
    assert product_fixture.id
    await ProductController().delete(_id=product_fixture.id)
    product = await ProductController.get(id=product_fixture.id)
    assert product is None
