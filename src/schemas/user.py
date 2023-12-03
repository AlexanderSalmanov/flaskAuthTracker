from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(required=True)
    email = fields.Email(required=True)
    num_visits = fields.Int(required=True)


user_schema = UserSchema()
