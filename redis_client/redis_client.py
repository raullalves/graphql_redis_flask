from redis_client.redis_decorator import connect_to_redis


class RedisClient(object):
    def __init__(self, host, port, db):
        self.port = port
        self.host = host
        self.db = db
        self.redis_connection = None

    @connect_to_redis
    def set_value(self, key, value):
        self.redis_connection.set(key, value)

    @connect_to_redis
    def get_value(self, key):
        value = self.redis_connection.get(key)
        if value is None:
            return None

        return value.decode('utf8')

    @connect_to_redis
    def set_dict(self, key, properties_dict):
        self.redis_connection.hmset(key, properties_dict)

    @connect_to_redis
    def get_dict(self, key):
        redis_dict = self.redis_connection.hgetall(key)
        decoded_dict = {k.decode('utf8'): v.decode('utf8') for k, v in redis_dict.items()}

        return decoded_dict

    @connect_to_redis
    def get_all_keys(self):
        keys = self.redis_connection.keys()

        return keys
