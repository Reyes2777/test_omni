import factory

from omni.models import User, Product, Order


class UserFactory(factory.Factory):
    first_name = 'Jonathan'
    last_name = 'Reyes'
    email = 'jonat@gmail.com'
    mobile_phone = '3503351227'

    class Meta:
        model = User


class ProductFactory(factory.Factory):
    name = 'Ballon'
    value = 10000

    class Meta:
        model = Product

