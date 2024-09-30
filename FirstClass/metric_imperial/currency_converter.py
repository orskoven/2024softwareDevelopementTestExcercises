import requests

class CurrencyConverter:
    def __init__(self, base_currency):
        """
        Constructor
        @param base_currency: The base currency in 3-letter format (e.g., 'DKK')
        """
        self.base_currency = base_currency.upper()
        self.api_key = 'YOUR_API_KEY'  # Replace with your freecurrencyapi.net API key

    def convert(self, amount, target_currency):
        """
        Converts the amount from base_currency to target_currency using the API.
        @param amount: The numeric amount to convert with up to two decimals
        @param target_currency: The currency to convert to
        @return: The converted monetary amount with up to two decimals
        """
        amount = round(amount, 2)
        target_currency = target_currency.upper()
        url = 'https://api.freecurrencyapi.net/v1/latest'
        params = {
            'apikey': self.api_key,
            'base_currency': self.base_currency,
            'currencies': target_currency
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            rate = data['data'][target_currency]
            converted_amount = amount * rate
            return round(converted_amount, 2)
        else:
            raise Exception("API request failed with status code " + str(response.status_code))