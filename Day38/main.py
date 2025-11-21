import requests, truststore, os, pyperclip
from datetime import datetime
truststore.inject_into_ssl()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import json
from pydantic import SecretStr
from dotenv import load_dotenv

# load_dotenv()  # either load each time to run after making a .env file, and then loading it, or store parmanantly in env variables

# Initialize Groq LLM
groq_key = os.environ.get("GROQ_API_KEY")     
# or setx GROQ_API_KEY "your_key_here" (in ps) to store it parmanantly as an env variable in os. 
# (or either store it as user variables from GUI, under environment variables)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
)


# Define the expected JSON structure
parser = JsonOutputParser(pydantic_object={
    "type": "object",
    "properties": {
        "exercise name": {"type": "string"},
        "calories burnt": {"type": "number"},
        "description": {"type": "string"},
        'duration': {"type": "number"}
        }
    }
)

# Create a simple prompt

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a calories tracker agent. The user gives you input of how much exercises they did.
    You need to estimate the calories burnt for each of the exercises in the given format:
    {{[
        {{
            "exercise name": "exercise name here",
            "calories burnt": exact number here,
            "description": "A one-two liner description of the calculation",
            "duration": "Duration of exercises in minutes (if given by user, else leave blank)"
        }},
        ...
    ]}}"""),
    ("user", "{input}")
])


# Create the chain that guarantees JSON output
chain = prompt | llm | parser

def parse_exercises(user_input):
    result = chain.invoke({"input": user_input})
    # print(result)
    # output_json = json.dumps(result, indent=2)
    # pyperclip.copy(output_json)
    return(result)
    

calories_count = parse_exercises(user_input=input('What all exercises you did today? '))
# print(calories_count, type(calories_count))

# print(calories_count[0])

# headers = {
#     'x-app-id': 'app_14ded99b1be2461293830c6b',
#     'x-app-key': 'nix_live_MVeNcEuBBwiFuKLtQrU4j1i2FhRtuznr',    
# }

# base_url = 'https://app.100daysofpython.dev'

# # POST Request - Calculate calories burned from a natural language exercise description.
# post_endpoint = f'{base_url}/v1/nutrition/natural/exercise'
# data = {
#     "query": input('What all exercises you did?'),
#     "weight_kg": 70,                  
#     "height_cm": 175,                 
#     "age": 21,                       
#     "gender": "male"
# }

# response = requests.post(url=post_endpoint, json=data, headers=headers)
# result = response.json()
# print(result)



# Get Today's date
now = datetime.now()
today = now.strftime('%d/%m/%Y')
time = now.strftime("%H:%M:%S")

# Post to sheety
sheety_post_endpoint= 'https://api.sheety.co/f7a06b26351ebc9265641f8b9c7c435a/workoutTracking/sheet1'
for i in calories_count:
    data2  = {
        "sheet1":{
            "date" : today,
            "time" : time,
            "exercise" : i["exercise name"],
            "duration" : i["duration"],
            "calories": i["calories burnt"]
        }
    }

    headers = {
    "Content-Type": "application/json"
    }

    sheet_response = requests.post(sheety_post_endpoint, json=data2, headers=headers)

    print(sheet_response.text)