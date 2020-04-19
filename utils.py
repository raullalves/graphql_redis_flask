import random
import string


def generate_random_string(qtd_of_digits=40, options=string.ascii_uppercase +
                                                     string.ascii_lowercase +
                                                     string.digits):
    return ''.join(random.choice(options) for _ in range(qtd_of_digits))
