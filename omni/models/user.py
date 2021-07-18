from tortoise import Model, fields


class User(Model):
    id = fields.IntField(pk=True)
    first_name = fields.TextField()
    last_name = fields.TextField()
    mobile_phone = fields.TextField()
    email = fields.TextField()
