import os, requests, truststore
from dotenv import load_dotenv

load_dotenv()
truststore.inject_into_ssl()
AMADEUS_API_KEY = os.environ.get('AMADEUS_API_KEY')
AMADEUS_API_SECRET = os.environ.get('AMADEUS_API_SECRET')

# print(AMADEUS_API_KEY, AMADEUS_API_SECRET)

class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    def __init__(self) -> None:
        pass

    def req_access_token(self):
        url = 'https://test.api.amadeus.com/v1/security/oauth2/token'
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
        "grant_type": "client_credentials",
        "client_id": AMADEUS_API_KEY,
        "client_secret": AMADEUS_API_SECRET,
        }

        self.response = requests.post(url, headers=headers, data=data)
        print(type(self.response))
        self.token_data = self.response.json()
        print(self.token_data)
        self.token = self.token_data["access_token"]

        return self.token