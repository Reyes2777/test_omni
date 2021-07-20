from pytest import mark

from omni.controllers.user import UserController


@mark.parametrize('data', (
        ({"first_name": "Jonathan", "last_name": "Reyes", "email": "jonat@gmail.com",
          "mobile_phone": "3503351227", 'response': 'User already exist'},
         {"first_name": "Jonathan", "last_name": "Reyes", "email": "jonathan@gmail.com",
         "mobile_phone": "3503351227", 'response': 'Successfully created User'}
         )))
@mark.asyncio
async def test_create_user(db_transaction, user_fixture, data):
    message_expected = data.pop('response')
    user_controller = UserController()
    user, message = await user_controller.create(**data)
    assert message_expected == message
    assert user.first_name == data['first_name']
    assert user.last_name == data['last_name']
    assert user.mobile_phone == data['mobile_phone']
    assert user.email == data['email']


@mark.asyncio
async def test_create_user_without_email(db_transaction):
    data = {
        "first_name": "Jonathan",
        "last_name": "Reyes",
        "mobile_phone": "3503351227"
    }
    user_controller = UserController()
    user, message = await user_controller.create(**data)
    assert user is None
    assert "Error" in message


@mark.asyncio
async def test_create_user_fail(db_transaction):
    data = {
        "first_name": "Jonathan",
        "email": 'jonathan.reyes“gmail.com',
        "mobile_phone": "3503351227"
    }
    user_controller = UserController()
    user, message = await user_controller.create(**data)
    assert user is None
    assert "Error" in message


@mark.asyncio
async def test_get_user(db_transaction, user_fixture):
    user = await UserController.get(id=user_fixture.id)
    assert user.first_name == 'Jonathan'
    assert user.email =='jonat@gmail.com'


@mark.asyncio
async def test_get_user_none(db_transaction):
    user = await UserController.get(id=0)
    assert user is None


@mark.asyncio
async def test_update_user(db_transaction, user_fixture):
    data = {
        "first_name": "Alejandro",
        "email": 'jonathan@gmail.com',
        "mobile_phone": "3503351227"
    }
    user = await UserController().update(_id=user_fixture.id, **data)
    assert user.first_name == 'Alejandro'
    assert user.email == 'jonat@gmail.com'
    assert user.id == user_fixture.id


@mark.asyncio
async def test_delete(db_transaction, user_fixture):
    assert user_fixture.id
    await UserController().delete(_id=user_fixture.id)
    user = await UserController.get(id=user_fixture.id)
    assert user is None
