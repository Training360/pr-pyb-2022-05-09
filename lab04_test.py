# teszteset == függvény
from lab04 import absolute, is_not_negative


def test_with_negative_number():
    # given
    number = -10
    # when
    result = is_not_negative(number)
    # then
    assert result == False

def test_with_positive_number():
    # given
    number = 10
    # when
    result = is_not_negative(number)
    # then
    assert result == True

def test_with_zero():
    assert is_not_negative(0) == True


def test_absolute_with_positive():
    assert absolute(10) == 10


def test_absolute_with_negative():
    assert absolute(-10) == 10