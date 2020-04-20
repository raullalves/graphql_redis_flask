import jwt

from graphene import ObjectType, Mutation, String, Boolean
from werkzeug.security import safe_str_cmp
from redis_client.redis_manager import redis_users


class CreateToken(Mutation):
    class Arguments:
        username = String()
        password = String()

    success = Boolean()
    token = String()

    @staticmethod
    def mutate(root, info, username, password):
        pass_redis = redis_users.get_value(username)
        if pass_redis is None:
            return {'success': False, 'token': ''}

        if not safe_str_cmp(pass_redis.encode('utf-8'), password.encode('utf-8')):
            return {'success': False, 'token': ''}

        encoded_jwt = jwt.encode({'user': username}, 'my_super_secret_key', algorithm='HS256')

        success = True
        token = encoded_jwt
        response_dict = {'success': success, 'token': token}
        return response_dict


class Mutation(ObjectType):
    login = CreateToken.Field()
