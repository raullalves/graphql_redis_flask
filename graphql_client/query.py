from graphene import ObjectType, String, Field, List

from graphql_client.authenticator import authenticate
from schemas.client import Client, ClientValueObject
from redis_client.redis_manager import redis_clients, redis_credit_card_information


class Query(ObjectType):
    client = Field(Client, id=String(required=True))
    clients = List(Client)

    @staticmethod
    @authenticate
    def resolve_client(parent, info, id):
        redis_response = redis_clients.get_dict(id)
        credit_card_information = redis_credit_card_information.get_dict(redis_response['ccid'])
        return ClientValueObject(firstname=redis_response['firstname'],
                                 lastname=redis_response['lastname'],
                                 age=redis_response['age'],
                                 city=redis_response['city'],
                                 id=redis_response['id'],
                                 creditcardnumber=credit_card_information['number'],
                                 cvv=credit_card_information['cvv'])

    @staticmethod
    @authenticate
    def resolve_clients(parent, info):
        ids = redis_clients.get_all_keys()
        response = []
        for id in ids:
            user_info = redis_clients.get_dict(id)
            credit_card_information = redis_credit_card_information.get_dict(user_info['ccid'])
            user_info['creditcardnumber'] = credit_card_information['number']
            user_info['cvv'] = credit_card_information['cvv']
            response.append(user_info)

        return response