import functools
import redis


def connect_to_redis(f):
    @functools.wraps(f)
    def redis_connector_wrapper(redis_client_instance, *args, **kwargs):
        if redis_client_instance.redis_connection is None:

            try:
                redis_client_instance.redis_connection = redis.Redis(host=redis_client_instance.host,
                                                                     port=redis_client_instance.port,
                                                                     db=redis_client_instance.db)
            except Exception as e:
                raise Exception('Failed to establish connection to redis at host {}, port {} and db {}'
                                .format(redis_client_instance.host,
                                        redis_client_instance.port,
                                        redis_client_instance.db))
        return f(redis_client_instance, *args, **kwargs)

    return redis_connector_wrapper


class RedisClient(object):
    def __init__(self, host, port, db):
        self.port = port
        self.host = host
        self.db = db
        self.redis_connection = None

    @connect_to_redis
    def set(self, key, properties_dict):
        self.redis_connection.hmset(key, properties_dict)

    @connect_to_redis
    def get(self, key):
        redis_dict = self.redis_connection.hgetall(key)
        decoded_dict = {k.decode('utf8'): v.decode('utf8') for k, v in redis_dict.items()}

        return decoded_dict
