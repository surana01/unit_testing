from unittest.mock import patch, Mock
from example_code.mock_tests.mock_api_calls.weather import get_weather

################################################################################
# Mocking with unittest.mock's `patch` decorator
################################################################################
@patch("example_code.mock_tests.mock_api_calls.weather.requests.get")
def test_get_weather_with_mocked_requests(mock_get):
    """
    Test the `get_weather` function with the `requests.get` call mocked.

    Demonstrates:
    -------------
    - Using `@patch` to replace `requests.get` with a mock object.
    - Controlling mock return values to simulate API responses.
    - Asserting that the mocked function was called with the correct arguments.
    """
    # Create a mock response object
    mock_response = Mock()
    mock_response.json.return_value = {"temp": 25, "desc": "Sunny"}
    mock_response.raise_for_status = Mock()

    # Set `requests.get` to return this mock response
    mock_get.return_value = mock_response

    # Call the function under test
    data = get_weather("London")

    # Assertions
    assert data == {"temp": 25, "desc": "Sunny"}
    mock_get.assert_called_once_with("https://api.example.com/weather?city=London")
    mock_response.raise_for_status.assert_called_once()


################################################################################
# Mocking with pytest-mock's `mocker` fixture
################################################################################
def test_get_weather_with_mocker(mocker):
    """
    Same behavior as the original test above, but using pytest-mock's `mocker` fixture.
    """
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"temp": 25, "desc": "Sunny"}
    mock_response.raise_for_status = mocker.Mock()

    mock_get = mocker.patch("requests.get")
    mock_get.return_value = mock_response

    data = get_weather("London")

    assert data == {"temp": 25, "desc": "Sunny"}
    mock_get.assert_called_once_with("https://api.example.com/weather?city=London")
    mock_response.raise_for_status.assert_called_once()