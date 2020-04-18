from collections import namedtuple

from graphene import ObjectType, String, Field

from redis_client.redis_client import RedisClient

ClientValueObject = namedtuple('Client', ['name', 'full_name', 'age', 'city'])


class Client(ObjectType):
    name = String()
    full_name = String()
    age = String()
    city = String()


class Query(ObjectType):
    client = Field(Client, id=String(required=True))

    @staticmethod
    def resolve_client(parent, info, id):
        redis_response = RedisClient().get(id)
        return ClientValueObject(name=redis_response['name'],
                                 full_name=redis_response['full_name'],
                                 age=redis_response['age'],
                                 city=redis_response['city'])
