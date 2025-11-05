"""This file contains fixtures that can be shared across test files."""

import pytest
from example_code.basic_tests.calculator import Calculator


@pytest.fixture(scope="function")  # default option
def calc_shared():
    """Provides a fresh Calculator instance for each test."""
    return Calculator()
