from datetime import datetime

from testy.funkcje import dodawanie, div, analyze_pesel
import pytest



@pytest.mark.parametrize("a, b, wynik", [
    (1, 1, 2),
    (2, 2, 4),
    (3, 3, 6),
    (0, 0, 0),
    (1, 2, 3),
    (2, 1, 3),
])
def test_dodawanie_1_1(a, b, wynik):
    assert dodawanie(a, b) == wynik


def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)


def test_pesel():
    assert analyze_pesel("44051401458")['pesel'] == "44051401458"

def test_pesel_data():
    assert analyze_pesel("44051401458")['birth_date'] == datetime(1944, 5, 14)

@pytest.mark.parametrize("pesel, data", [
    ('31220552363', datetime(2031, 2, 5)),
    ('94231748464', datetime(2094, 3, 17)),
    ('52262929533', datetime(2052, 6, 29)),
    ('85272818845', datetime(2085, 7, 28)),
    ('82321745866', datetime(2082, 12, 17)),
])
def test_dates_pesel(pesel, data):
    assert analyze_pesel(pesel)['birth_date'] == data



def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


def test_leap_year():
    assert is_leap_year(2000)

def test_leap_year2():
    assert is_leap_year(2004)

def test_leap_year3():
    assert is_leap_year(2008)