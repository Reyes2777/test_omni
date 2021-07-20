from omni.controllers.base import BaseController
from omni.models import Order


class OrderController(BaseController):
    _model = Order
    _name = 'Order'
