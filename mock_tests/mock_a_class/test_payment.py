from unittest.mock import Mock
from payment import process_payment

################################################################################
# Mocking with unittest.mock's `Mock` class
################################################################################
def test_process_payment_success():
    """
    Test `process_payment` with a successful mock charge.

    Demonstrates:
    -------------
    - How to mock an object with methods.
    - How to simulate both successful and failed scenarios.
    """
    mock_gateway = Mock()
    mock_gateway.charge.return_value = None  # Simulate success

    result = process_payment(100, mock_gateway)

    assert result == "success"
    mock_gateway.charge.assert_called_once_with(100)


def test_process_payment_failure():
    """
    Test `process_payment` when the gateway raises an exception.

    Demonstrates:
    -------------
    - How to simulate errors using `side_effect`.
    - How to ensure error handling logic works correctly.
    """
    mock_gateway = Mock()
    mock_gateway.charge.side_effect = Exception("Network error")

    result = process_payment(100, mock_gateway)

    assert result == "failure"
    mock_gateway.charge.assert_called_once_with(100)


################################################################################
# Mocking with pytest-mock's `mocker` fixture
################################################################################
def test_process_payment_success_with_mocker(mocker):
    """
    Same behavior as the original test above, but using pytest-mock's `mocker` fixture.
    """
    mock_gateway = mocker.Mock()
    mock_gateway.charge.return_value = None

    result = process_payment(100, mock_gateway)

    assert result == "success"
    mock_gateway.charge.assert_called_once_with(100)
    

def test_process_payment_failure_with_mocker(mocker):
    """
    Same behavior as the original test above, but using pytest-mock's `mocker` fixture.
    """
    mock_gateway = mocker.Mock()
    mock_gateway.charge.side_effect = Exception("Network error")

    result = process_payment(100, mock_gateway)

    assert result == "failure"
    mock_gateway.charge.assert_called_once_with(100)