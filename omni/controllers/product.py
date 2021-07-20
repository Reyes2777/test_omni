from omni.controllers.base import BaseController
from omni.models import Product


class ProductController(BaseController):
    _model = Product
    _name = 'Product'
