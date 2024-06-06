import pytest


def prime_number(n):
    lst = []
    diveder = 2
    while n > 1:
        while n % diveder == 0:
            lst.append(diveder)
            n = n // diveder
        diveder += 1
    return lst


@pytest.mark.parametrize('n, result', [
    (1, []),
    (2, [2]),
    (3, [3]),
    (4, [2, 2]),
    (5, [5]),
    (6, [2, 3]),
    (7, [7]),
    (8, [2, 2, 2]),
    (9, [3, 3]),
    (2*2*2*3*3*5*7*11*13, [2,2,2,3,3,5,7,11,13]),
])
def test_prime_number(n, result):
    assert prime_number(n) == result

def length(password):
    return len(password) >= 7

def upper(password):
    return any(x.isupper() for x in password)

def lower(password):
    return any(x.islower() for x in password)

def special_sing(password):
    return any(x for x in password if x in """!@#$%^&*()_+-={}[]|\:";'<>?,./""")

def digit(password):
    return any(x.isdigit() for x in password)
def validate_password(password):
    validators = [length, upper, lower, special_sing, digit]
    for validation in validators:
        if not validation(password):
            return False

def hash_password(password):
    if validate_password(password):
        return hash(password)

