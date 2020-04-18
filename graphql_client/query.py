from collections import namedtuple

from graphene import ObjectType, String, Field

from redis_client.redis_manager import redis_clients

ClientValueObject = namedtuple('Client', ['name', 'fullName', 'age', 'city'])


class Client(ObjectType):
    name = String()
    fullName = String()
    age = String()
    city = String()


class Query(ObjectType):
    client = Field(Client, id=String(required=True))

    @staticmethod
    def resolve_client(parent, info, id):
        redis_response = redis_clients.get(id)
        return ClientValueObject(name=redis_response['name'],
                                 fullName=redis_response['fullName'],
                                 age=redis_response['age'],
                                 city=redis_response['city'])
