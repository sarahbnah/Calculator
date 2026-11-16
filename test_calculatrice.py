import pytest
from calculatrice import addition, division


def test_addition():
    assert addition(5, 3) == 8


def test_division():
    assert division(10, 2) == 5


def test_division_par_zero():
    with pytest.raises(ValueError):
        division(10, 0)