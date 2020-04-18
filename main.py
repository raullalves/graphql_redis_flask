from redis_client.redis_client import RedisClient
from utils import generate_random_string_key


def create_client(name, age):
    client_key = generate_random_string_key()
    client_dict = {'name': name, 'age': age}

    return client_key, client_dict


def populate_redis():
    client_A_key, client_A_dict = create_client(name='Robert', age=25)
    RedisClient().set(client_A_key, client_A_dict)


def main():
    populate_redis()


if __name__ == '__main__':
    main()
