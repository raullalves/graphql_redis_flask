import string

from utils import generate_random_string

usernames = [generate_random_string(qtd_of_digits=5) for _ in range(50)]
passwds = [generate_random_string(qtd_of_digits=15) for _ in range(50)]

first_names = ['Alberto',
               'Bruna',
               'Chad',
               'Denise',
               'Elliot',
               'Felipe',
               'Georgia',
               'Heitor',
               'Ian',
               'John',
               'Kelly',
               'Luis',
               'Maurice',
               'Neil']

last_names = ['Alves',
              'Brown',
              'Connor',
              'Santiago',
              'Richard',
              'Menezes',
              'de Mello']

cities = ['Rio de Janeiro',
          'New York',
          'New Delhi',
          'Tokyo',
          'Sydney',
          'Beijing',
          'Dublin']

ages = [i for i in range(18, 60)]


credit_card_numbers = [generate_random_string(qtd_of_digits=15, options=string.digits)
                       for _ in range(50)]

cvvs = [generate_random_string(qtd_of_digits=3, options=string.digits)
                       for _ in range(50)]

