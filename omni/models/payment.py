from tortoise import Model, fields


class Payment(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('omni.User', related_name='user_payment', unique=True)
    value = fields.IntField()
    created = fields.DatetimeField(auto_now_add=True)
