from tortoise import Model, fields

from omni.models.todict import ToDict


class Product(ToDict, Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    value = fields.DecimalField(max_digits=10, decimal_places=2)
