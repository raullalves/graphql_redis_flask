from redis_client.redis_decorator import connect_to_redis


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

    @connect_to_redis
    def get_all(self):
        keys = self.redis_connection.keys()
        users_list = []
        for key in keys:
            user_dict = self.get(key)
            users_list.append(user_dict)

        return users_list