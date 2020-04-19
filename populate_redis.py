import random
from random_info import *
from redis_client.redis_manager import redis_clients, redis_credit_card_information, redis_users


def create_clients(qtd_of_clients=50):
    for _ in range(qtd_of_clients):
        client_key = generate_random_string()
        credit_card_key = generate_random_string()

        client_first_name = random.choice(first_names)
        client_last_name = random.choice(last_names)
        client_city = random.choice(cities)
        client_age = random.choice(ages)

        credit_card_number = random.choice(credit_card_numbers)
        credit_card_cvv = random.choice(cvvs)

        client_dict = {'id': client_key,
                       'firstname': client_first_name,
                       'lastname': client_last_name,
                       'age': client_age,
                       'city': client_city,
                       'ccid': credit_card_key}

        credit_card_dict = {'id': credit_card_key,
                            'number': credit_card_number,
                            'cvv': credit_card_cvv}

        redis_clients.set_dict(client_key, client_dict)
        redis_credit_card_information.set_dict(credit_card_key, credit_card_dict)


def create_login_data(qtd_of_users=20):
    for _ in range(qtd_of_users):
        username = random.choice(usernames)
        passw = random.choice(passwds)
        redis_users.set_value(username, passw)

    redis_users.set_value('admin', 'admin')


def create_client(name, fullname, age, city):
    client_key = generate_random_string()

    client_dict = {'id': client_key,
                   'name': name,
                   'fullname': fullname,
                   'age': age,
                   'city': city}

    return client_key, client_dict


def main():
    create_clients()
    create_login_data()


if __name__ == '__main__':
    main()
