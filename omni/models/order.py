from tortoise import Model, fields


class Order(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('omni.User', related_name='user_order', unique=True)
    created = fields.DatetimeField(auto_now_add=True)
    products = fields.ForeignKeyField('omni.Product', related_name='products_order')