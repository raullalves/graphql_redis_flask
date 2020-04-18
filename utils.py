def generate_random_string_key(qtd_of_digits=15):
    import random
    import string
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(qtd_of_digits))
