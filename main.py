from redis_client.redis_manager import redis_clients
from utils import generate_random_string_key


def create_client(name, fullName, age, city):
    client_key = generate_random_string_key()

    client_dict = {'name': name,
                   'fullName': fullName,
                   'age': age,
                   'city': city}

    return client_key, client_dict


def populate_redis():
    client_A_key, client_A_dict = create_client(name='Robert',
                                                fullName='Robert Silva',
                                                age=25,
                                                city='London')

    redis_clients.set(client_A_key, client_A_dict)

    client_B_key, client_B_dict = create_client(name='Maria',
                                                fullName='Maria Jhones',
                                                age=44,
                                                city='Buenos Aires')

    redis_clients.set(client_B_key, client_B_dict)


def main():
    populate_redis()


if __name__ == '__main__':
    main()
