from tortoise import Model, fields

from omni.models.todict import ToDict


class Shipment(ToDict, Model):
    id = fields.IntField(pk=True)
    orders = fields.ForeignKeyField('omni.Order', related_name='orders_shipment')
    created = fields.DatetimeField()
