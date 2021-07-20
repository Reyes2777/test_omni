import factory

from omni.models import User


class UserFactory(factory.Factory):
    first_name = 'Jonathan'
    last_name = 'Reyes'
    email = 'jonat@gmail.com'
    mobile_phone = '3503351227'

    class Meta:
        model = User
