import pandas as pd
"""
Readability >> Premature Optimization 

with open('weather.csv') as data_file:
    data = data_file.readlines()
    print(data)

import csv

with open('weather.csv') as data_file:
    data = csv.reader(data_file)
    print(data)            # <_csv.reader object at 0x000002CF18CB2C80>
    
    temperatures = []
    for row in data:
        # print(row)
        if row[1] != 'temp':
            temp = int(row[1])
            temperatures.append(temp)
    print(temperatures)


# Pandas Library


data = pandas.read_csv("Day25/weather.csv")
# print(data)

# print(data['temp'])
print(type(data))
print(type(data['temp']))

# two datastructures in pandas, series and dataframes

# https://pandas.pydata.org/docs/reference/index.html#api

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(len(temp_list))
print('avg_temp = ',round(sum(temp_list)/len(temp_list) ,2))

print(data['temp'].mean()) 
print(data['temp'].max())    #useful methods in pandas library

print(data['condition'])   # OR
print(data.condition)           # headings converted to attributes in backend

# get data in row 
print(data[data.day == 'Monday'])

x = data.temp == data.temp.max()     # returns True or False for each row in df
print(data[x])             # <5  Saturday    16  Overcast>

monday = data[data.day == 'Monday']
print(monday)
print(monday.condition)

monday_temp = monday.temp[0]          #though this monday.temp will only be a singleton list
monday_temp_farenheit = 9/5*monday_temp + 32

print(monday_temp_farenheit)



# Create Dataframe from Scratch

data_dict = {
    'students': ['amy', 'james', 'angela'],
    'scores' : [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)

data.to_csv('Day25/new_data.csv')
"""

with open('Day25/squirrel-data.csv', 'r') as f:
    df = pd.read_csv(f, encoding="utf-8-sig")
    # print(df.head(5))

    # print(df.info())
    print(df.describe())
    print(df.shape)

    print(df.columns)

    df_
































