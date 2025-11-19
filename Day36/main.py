# BSE - Stock news alert

# 1. Pull in the stocks price through some API.
# 2. Pull the closing price at the day, and at the previous day
# 3. Calculate the percentage change (and direction)
# 4. When there is some extraordinary change (>=10%), fetch some relevant news about the company through an API
# 5. Send an SMS, telling what was the big fluctuation happened, and what was the news regarding this.

import requests, truststore, pyperclip
from datetime import datetime, timedelta
truststore.inject_into_ssl()

company_name = 'Amazon'

def stock_symbol(company_name):
    url = 'https://www.alphavantage.co/query'
    params={
        'function': 'SYMBOL_SEARCH',
        'keywords':company_name,
        'apikey':'87Q1JEXLFIBZ2IYY',
    }
    r = requests.get(url, params=params)
    data = r.json()
    print(data)
    # return data['bestMatches'][0]['1. symbol']
print(stock_symbol('Amazon'))

#alphavantage api 87Q1JEXLFIBZ2IYY   news_api 0326bb771be8402bb4b2f434f4e5ec67
url = 'https://www.alphavantage.co/query'
params={
    'function': 'TIME_SERIES_DAILY',
    'symbol': stock_symbol(company_name),
    'apikey':'87Q1JEXLFIBZ2IYY',
}

r = requests.get(url, params=params)
data = r.json()
# print(data)
now = datetime.now()
print(now.weekday())

def yesterday():
    if now.weekday() == 0:
        days = 3
    elif now.weekday() == 6:
        days = 2
    else:
        days = 1
    yesterday = now - timedelta(days)
    yesterday_str = yesterday.strftime('%Y-%m-%d')
    return yesterday_str

def day_before():
    if now.weekday() == 0:
        days = 4
    elif now.weekday() == 1:
        days = 4
    else:
        days = 2
    day_before = now - timedelta(days)
    day_before_str = day_before.strftime('%Y-%m-%d')
    return day_before_str

# print(yesterday_str, day_before_str)
yesterday_str = yesterday()
day_before_str = day_before()
today_str = now.strftime('%Y-%m-%d')

yest_close_price = float(data['Time Series (Daily)'][yesterday_str]['4. close'])
day_before_close_price = float(data['Time Series (Daily)'][day_before_str]['4. close'])
last_refreshed = data['Meta Data']['3. Last Refreshed']

print(f'Company {company_name} had price {yest_close_price} at yesterday closing, and {day_before_close_price} at day-before (working) closing. Data last refreshed on: {last_refreshed}')

def calculations():
    diff = round((yest_close_price - day_before_close_price),2)
    # print(diff)
    if diff < 0:
        symbol = '📉'
    elif diff == 0:
        symbol = None
    else:
        symbol = '📈'

    abs_diff = abs(diff)
    # print(abs_diff)

    perc_change = round(abs_diff/yest_close_price ,2)
    print(symbol)
    return perc_change


def trigger_news():

    url = "https://newsapi.org/v2/everything"

    params = {
        "pageSize": 3,
        "apiKey": "0326bb771be8402bb4b2f434f4e5ec67",
        "q": company_name,
        'from': day_before_str,
        'to': today_str,
    }

    response = requests.get(url, params=params)
    data2 = response.json()
    pyperclip.copy(data2)
    # print(response.json())   # response data
    news_list = []
    for i in data2['articles']:
        news_list.append(i['description'])

    formatted_news = f'Headlines \n 1. {news_list[0]} \n 2. {news_list[1]} \n 3. {news_list[2]}'
    return formatted_news

# result = calculations()
# if result >= 10:
#     trigger_news()


trigger_news()
