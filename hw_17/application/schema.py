from marshmallow import Schema, fields
#модели для сериализации

class Movie (Schema):
    id = fields.Int(dump_only=True) #тк id передается в строке запроса
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    raiting = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()

class Director (Schema):
    id = fields.Int(dump_only=True) #тк id передается в строке запроса
    name = fields.Str()

class Genre (Schema):
    id = fields.Int(dump_only=True)  # тк id передается в строке запроса
    name = fields.Str()
