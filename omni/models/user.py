from tortoise import Model, fields

from omni.models.todict import ToDict


class User(ToDict, Model):
    id = fields.IntField(pk=True)
    first_name = fields.TextField()
    last_name = fields.TextField()
    mobile_phone = fields.TextField()
    email = fields.TextField()
