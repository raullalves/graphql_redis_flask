import jwt
import functools

from redis_client.redis_manager import redis_users


def authenticate(f):
    @functools.wraps(f)
    def authenticator(*args, **kwargs):
        authorization_token = args[1].context.headers.get('Authorization', None)
        if authorization_token is None:
            raise Exception('Missing user authorization')

        decoded_user_info = jwt.decode(authorization_token, 'my_super_secret_key', algorithms=['HS256'])
        user = decoded_user_info.get('user', None)

        if user and redis_users.get_value(user):
            return f(*args, **kwargs)

        raise Exception('Invalid token')

    return authenticator
