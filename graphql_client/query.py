from collections import namedtuple

from graphene import ObjectType, String, Field, List

from redis_client.redis_manager import redis_clients

ClientValueObject = namedtuple('Client', ['name', 'fullname', 'age', 'city', 'id'])


class Client(ObjectType):
    name = String()
    fullname = String()
    age = String()
    city = String()
    id = String()


class Query(ObjectType):
    client = Field(Client, id=String(required=True))
    clients = List(Client)

    @staticmethod
    def resolve_client(parent, info, id):
        redis_response = redis_clients.get(id)
        return ClientValueObject(name=redis_response['name'],
                                 fullname=redis_response['fullname'],
                                 age=redis_response['age'],
                                 city=redis_response['city'],
                                 id=redis_response['id'])

    @staticmethod
    def resolve_clients(parent, info):
        return redis_clients.get_all()
