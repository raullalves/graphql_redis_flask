from graphene import ObjectType, String, Field, List

from graphql_client.authenticator import authenticate
from schemas.client import Client, ClientValueObject
from redis_client.redis_manager import redis_clients


class Query(ObjectType):
    client = Field(Client, id=String(required=True))
    clients = List(Client)

    @staticmethod
    @authenticate
    def resolve_client(parent, info, id):
        redis_response = redis_clients.get_dict(id)
        return ClientValueObject(name=redis_response['name'],
                                 fullname=redis_response['fullname'],
                                 age=redis_response['age'],
                                 city=redis_response['city'],
                                 id=redis_response['id'])

    @staticmethod
    @authenticate
    def resolve_clients(parent, info):
        headers = info.context.headers
        return redis_clients.get_all_dicts()

