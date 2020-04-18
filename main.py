from redis_client.redis_client import RedisClient
from utils import generate_random_string_key


def create_client(name, full_name, age, city):
    client_key = generate_random_string_key()

    client_dict = {'name': name,
                   'full_name': full_name,
                   'age': age,
                   'city': city}

    return client_key, client_dict


def populate_redis():
    client_A_key, client_A_dict = create_client(name='Robert',
                                                full_name='Robert Silva',
                                                age=25,
                                                city='London')

    RedisClient().set(client_A_key, client_A_dict)

    client_B_key, client_B_dict = create_client(name='Maria',
                                                full_name='Maria Jhones',
                                                age=44,
                                                city='Buenos Aires')

    RedisClient().set(client_B_key, client_B_dict)


def main():
    populate_redis()


if __name__ == '__main__':
    main()
