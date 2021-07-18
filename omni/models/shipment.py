from tortoise import Model, fields


class Shipment(Model):
    id = fields.IntField(pk=True)
    orders = fields.ForeignKeyField('omni.Order', related_name='orders_shipment')
    created = fields.DatetimeField()
