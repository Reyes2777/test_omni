from omni.controllers.base import BaseController
from omni.models import User


class UserController(BaseController):
    _model = User
    _name = 'User'
