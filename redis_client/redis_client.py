import redis


class RedisClient(object):
    __instance = None

    def __new__(cls):
        if RedisClient.__instance is None:
            RedisClient.__instance = super(RedisClient, cls).__new__(cls)
            RedisClient.__instance.set_up_config()
            RedisClient.__instance.connect()
        return RedisClient.__instance

    def set_up_config(self):
        self.host = '192.168.99.100'
        self.port = 6379

    def connect(self):
        try:
            self.redis_connection = redis.Redis(host=self.host, port=self.port)
        except Exception as e:
            raise Exception('Failed to connect to Redis at host {} and port {}: '
                            .format(self.host, self.port, e))

    def set(self, key, properties_dict):
        self.redis_connection.hmset(key, properties_dict)

    def get(self, key):
        redis_dict = self.redis_connection.hgetall(key)
        decoded_dict = {k.decode('utf8'): v.decode('utf8') for k, v in redis_dict.items()}

        return decoded_dict
