from langchain.agents import tool
import requests


@tool
def get_stock_price(symbol: str):
    """Use this tool to get the current stock price for a company. Input should be the company stock symbol."""
    response = requests.get(f"https://api.stock.com/v1/quotes/{symbol}")
    if response.status_code == 200:
        data = response.json()
        return f"The current stock price of {symbol} is ${data['price']}."
    else:
        return "Sorry, I couldn't retrieve the stock information at this time."
