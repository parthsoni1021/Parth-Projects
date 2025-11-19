# API (Application Programming Interface) is a set of commands, functions, protocols, and objects
# that programmers can use to create software or interact with an external system 

MY_LAT = 28.644800
MY_LONG = 77.216721

import requests, datetime as dt
import truststore
truststore.inject_into_ssl()

# API endpoint - URL Address | API Parameter - input to the request
# print(response)   <Response [200]>

"""response codes: 
1XX: Hold on
2XX : Here you go
3XX : Go away
4XX : You screwed up
5XX : I screwed up

https://httpstatuses.com
"""

response = requests.get(url='http://api.open-notify.org/iss-now.json')
print(response.status_code)
response.raise_for_status()

data = response.json()
# print(data)
iss_longitude = data['iss_position']['longitude']
iss_latitude = data['iss_position']['latitude']
iss_position = (iss_longitude, iss_latitude)
print(iss_position)


def is_night():
    url = "https://api.sunrise-sunset.org/json"
    params = {
        'lat': MY_LAT, 
        'long': MY_LONG,
        "formatted": 0
    }

    response2 = requests.get(url, params=params)
    data2 = response2.json()
    # print(data)
    sunrise = int(data2['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data2['results']['sunset'].split('T')[1].split(':')[0])

    # print(sunrise, type(sunrise))         # UTC Time, for IST, add 5.30 hrs

    time_now = dt.datetime.now().hour
    if time_now>= sunset or time_now<=sunrise:
        return True
    
    # print(time_now, type(time_now))
    # print(sunrise)
    # print(sunset)
    # print(time_now.hour)

# If the ISS is close to my current position, and it is dark here, send an email to look up in the sky, and run this every 60 seconds

def is_iss_overhead():
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

if is_iss_overhead() and is_night():
    # send the email 
    pass















