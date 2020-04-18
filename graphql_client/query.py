from collections import namedtuple

from graphene import ObjectType, String, Field

from redis_client.redis_client import RedisClient

ClientValueObject = namedtuple("Client", ["name", "age"])


class Client(ObjectType):
    name = String()
    age = String()


class Query(ObjectType):
    me = Field(Client, id=String(required=True))

    @staticmethod
    def resolve_me(parent, info, id):
        r = RedisClient().get(id)
        return ClientValueObject(name=r['name'], age=r['age'])