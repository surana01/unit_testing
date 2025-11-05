from unittest.mock import Mock
from example_code.mock_tests.mock_simple_function.math_utils import (
    compute_discounted_price
)


################################################################################
# Mocking with unittest.mock's `Mock` class
################################################################################
def test_compute_discounted_price_with_mock():
    """
    Test `compute_discounted_price` using a mock discount provider.

    Demonstrates:
    -------------
    - How to inject a mock object into a function.
    - How to set return values on mocks.
    - How to assert that the mock was called.
    """
    # Create a mock discount provider
    mock_discount = Mock(return_value=0.2)

    result = compute_discounted_price(100, mock_discount)

    # Check the expected result
    assert result == 80.0

    # Verify the mock was called exactly once
    mock_discount.assert_called_once()


################################################################################
# Mocking with pytest-mock's `mocker` fixture
################################################################################
def test_compute_discounted_price_with_mocker(mocker):
    """
    Same behavior as the original test above, but using pytest-mock's `mocker` fixture.
    """

    # Note, this should be a fixture if used in several tests 
    discount_provider = mocker.Mock(return_value=0.2)

    result = compute_discounted_price(100, discount_provider)

    assert result == 80.0
    discount_provider.assert_called_once()