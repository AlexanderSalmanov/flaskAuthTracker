from marshmallow import Schema, fields


class AnonymousUserSchema(Schema):
    id = fields.Int(required=True)
    ip_address = fields.Str(required=True)
    num_visits = fields.Int()


anon_user_schema = AnonymousUserSchema()
