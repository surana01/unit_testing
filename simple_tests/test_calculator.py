# test_calculator.py
# ---------------------------------------------------
# Unit tests for the Calculator class (in calculator.py)
# These tests use pytest features like fixtures,
# parameterization, and exception checking.
# ---------------------------------------------------

import pytest
from calculator import Calculator


# ------------------------
# Fixture Example
# ------------------------
# Fixtures are pytest’s way of setting up reusable test resources.
# The fixture below creates a fresh Calculator instance for each test
# that uses it (pytest injects it automatically into test functions).
@pytest.fixture
def calc():
    """Provides a fresh Calculator instance for each test."""
    return Calculator()


# ------------------------
# Basic Operation Tests
# ------------------------
def test_add(calc):
    # Simple addition tests
    assert calc.add(3, 4) == 7
    assert calc.add(-1, 1) == 0


def test_subtract(calc):
    # Testing subtraction
    assert calc.subtract(10, 5) == 5


def test_multiply(calc):
    # Testing multiplication
    assert calc.multiply(2, 3) == 6


# ------------------------
# Parametrized Tests
# ------------------------
# @pytest.mark.parametrize allows you to easily test multiple
# input/output combinations without writing multiple test functions.
@pytest.mark.parametrize("a,b,result", [
    (10, 2, 5),
    (9, 3, 3),
])
def test_divide(calc, a, b, result):
    """Tests multiple valid division cases using parameterization."""
    assert calc.divide(a, b) == result


# ------------------------
# Testing Exceptions
# ------------------------
# Use pytest.raises to ensure specific errors are thrown under conditions.
def test_divide_by_zero(calc):
    """Ensure dividing by zero raises a ValueError."""
    with pytest.raises(ValueError):
        calc.divide(1, 0)


# ------------------------
# Testing List-Based Methods
# ------------------------
def test_average(calc):
    """Check that average of a non-empty list is computed correctly."""
    assert calc.average([1, 2, 3, 4]) == 2.5


def test_average_empty(calc):
    """Ensure average() raises a ValueError when list is empty."""
    with pytest.raises(ValueError):
        calc.average([])


# ------------------------
# Parametrized Power Tests
# ------------------------
# Here we test several base/exponent combinations at once.
# The final case intentionally exposes a hidden bug in the implementation!
@pytest.mark.parametrize("base,exp,expected", [
    (2, 3, 8),       # Normal positive exponent
    (5, 0, 1),       # Any number to the power of 0 = 1
    (2, -2, 0.25),   # Negative exponent — will FAIL due to hidden bug
])
def test_power(calc, base, exp, expected):
    """
    Tests the power() method for different exponent cases.
    The third case (2 ** -2) is expected to FAIL because
    the current implementation in Calculator.power()
    incorrectly returns 0 for negative exponents.
    """
    assert calc.power(base, exp) == pytest.approx(expected)
    # pytest.approx() is used to compare floating-point results
    # (e.g., 0.3333 vs 1/3) with a small tolerance.
