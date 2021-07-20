from omni.controllers.base import BaseController
from omni.models import Shipment


class ShipmentController(BaseController):
    _model = Shipment
    _name = 'Shipment'
