#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

"""
To do:
1. Make a list of places you want to visit in the google sheets
2. Get the IATA codes of the places, and set some random prices in the sheet
3. Link the sheet to get and post data in it
4. From the flight search API, get the prices of the flights. 
  # One city might have multiple airports, so get the city code, not airport's
  # Flight might stop at some intermediate city
5. POST those prices in the sheet for all the locations
6. Run a function which finds if there are any low prices 
7. If yes, send the details via SMS
"""

from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

# Request access token from Amadeus
flightsearch = FlightSearch()
token = flightsearch.req_access_token()




