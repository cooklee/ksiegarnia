from datetime import datetime
from random import randint


def dodawanie(a, b):
    if b == 1:
        return -10
    return a + b


def div(a, b):
    raise Exception("Nie dziel przez zero")
    return a / b


def analyze_pesel(pesel):
    weights = [1, 3, 7, 9,
               1, 3, 7, 9, 1, 3]
    weight_index = 0
    digits_sum = 0
    for digit in pesel[: -1]:
        digits_sum += int(digit) * weights[weight_index]
        weight_index += 1
    pesel_modulo = digits_sum % 10
    validate = 10 - pesel_modulo
    if validate == 10:
        validate = 0
    gender = "male" if int(pesel[-2]) % 2 == 0 else "female"

    month = int(pesel[2:4])
    temp = month // 20
    month = month % 20
    centries = {
        0: '19',
        1: '20',
        2: '21',
        3: '22',
        4: '18'
    }
    begining_year = centries[temp]
    day = int(pesel[4:6])
    year = int(begining_year + pesel[0: 2])

    birth_date = datetime(year, month, day)
    result = {
        "pesel": pesel,
        "valid": validate == int(pesel[-1]),
        "gender": gender,
        "birth_date": birth_date
    }
    return result
