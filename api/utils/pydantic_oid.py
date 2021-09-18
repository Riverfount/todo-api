from bson import ObjectId


class PyObjectId(ObjectId):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        try:
            return str(ObjectId(v))
        except Exception:
            raise TypeError('ObjectId required or invalid')

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')
