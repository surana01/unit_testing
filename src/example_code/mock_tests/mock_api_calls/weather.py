import requests

def get_weather(city):
    """
    Fetch current weather data for a given city using a REST API.

    Parameters
    ----------
    city : str
        The name of the city.

    Returns
    -------
    dict
        Parsed JSON response containing temperature and description.
    """
    response = requests.get(f"https://api.example.com/weather?city={city}")
    response.raise_for_status()
    return response.json()