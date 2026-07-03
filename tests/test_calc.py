from src.calculations import add_two_numbers, divide
import numpy as np

def test_add_positive_numbers():
    """Test adding two positive numbers."""
    result = add_two_numbers(5, 3)
    assert result == 8

def test_divide():
    result = divide(50, 10)
    assert result == 5


def test_divide_by_zero():
    result = divide(50, 0)
    assert result == "NA"


def test_divide_zero_by_zero():
    result = divide(0, 0)
    assert result == "NA"
