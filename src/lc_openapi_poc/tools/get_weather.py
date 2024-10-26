from langchain.agents import tool
import requests


@tool
def get_weather(city: str) -> str:
    """Use this tool to get the current weather for a specific city. Input should be the city name."""
    response = requests.get(f"https://api.weather.com/v3/wx/conditions/current?city={city}")
    if response.status_code == 200:
        data = response.json()
        return f"The current temperature in {city} is {data['temperature']}°C."
    else:
        return "Sorry, I couldn't retrieve the weather information at this time."
