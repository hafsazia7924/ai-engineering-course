import pytest


def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be zero")
    return a / b


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_divide_normal():
    assert divide(10, 2) == 5.0
#practical 1
def agecheck(age):
    if age<0:
        raise ValueError("Age can not be less than 0")
    return age
def test_negative_age():
    with pytest.raises(ValueError):
        agecheck(-5)
def test_normalage():
    assert agecheck(25)==25

#practical 2
def check_marks(marks):
    if marks<0 or marks>100:
        raise ValueError("Invalid Marks")
    return marks
def test_marks_below_0():
    with pytest.raises(ValueError):
        check_marks(-1)
def test_marks_above_100():
    with pytest.raises(ValueError):
        check_marks(101)
def test_checkmarksnormal():
    assert check_marks(75)==75