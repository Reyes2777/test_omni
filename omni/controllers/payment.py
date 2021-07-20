from omni.controllers.base import BaseController
from omni.models import Payment


class PaymentController(BaseController):
    _model = Payment
    _name = 'Payment'
