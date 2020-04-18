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