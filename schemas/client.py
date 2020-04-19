from collections import namedtuple

from graphene import ObjectType, String

ClientValueObject = namedtuple('Client', ['name', 'fullname', 'age', 'city', 'id'])


class Client(ObjectType):
    name = String()
    fullname = String()
    age = String()
    city = String()
    id = String()