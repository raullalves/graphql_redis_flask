from collections import namedtuple
from graphene import ObjectType, String

ClientValueObject = namedtuple('Client', ['id', 'firstname', 'lastname', 'age', 'city', 'creditcardnumber', 'cvv'])


class Client(ObjectType):
    id = String()
    firstname = String()
    lastname = String()
    age = String()
    city = String()
    creditcardnumber = String()
    cvv = String()
