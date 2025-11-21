# Pixela
import requests, truststore
# using requests module to make http requests at internet
# get, post, put (to Update), delete

truststore.inject_into_ssl()
url = 'https://pixe.la/v1/users'
TOKEN = 'ajhfuia2hrkjcviuhwejo'
USERNAME = 'parthsoni'

#STEP 1 - Create a user. New account set up

user_params = {
    'token': TOKEN,    # We need to make this
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=url, json=user_params)
# print(response.text)

# STEP2: Make a graph
graph_url = f'{url}/{USERNAME}/graphs'

graph_config = {
    'id':'graph1',
    'name':'PushUps Graph',
    'unit':'Nos',
    'type':'int',
    'color':'ajisai'
}

# Authentication using header is important
headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_url, json=graph_config, headers=headers)
# print(response.text)

#STEP3: Post a pixel on the graph
from datetime import datetime
now = datetime.now()
today = now.strftime("%Y%m%d")
# print(today)

post_url = 'https://pixe.la/v1/users/parthsoni/graphs/graph1'

pixel_config = {
    'date' : str(today),
    'quantity': str(20),
    # 'optionalData': {'coding also done': 'Yes'}
}

# response2 = requests.post(post_url, json=pixel_config, headers=headers)
# print(response2.text)


# Update

update_endpoint =f'https://pixe.la/v1/users/parthsoni/graphs/graph1/{now.strftime("%Y%m%d")}'

new_pixel_data = {
    'quantity': '5'
}

response3 = requests.put(update_endpoint, json=new_pixel_data, headers=headers)
print(response3.text)

# similarly use delete endpoint
# Does not take any body, only headers. It delete endpoint