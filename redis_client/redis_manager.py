from redis_client.redis_client import RedisClient

redis_users = RedisClient(host='192.168.99.100', port=6379, db=0)
redis_clients = RedisClient(host='192.168.99.100', port=6379, db=1)
redis_credit_card_information = RedisClient(host='192.168.99.100', port=6379, db=2)
