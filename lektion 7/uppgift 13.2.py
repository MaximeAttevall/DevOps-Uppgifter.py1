import requests
import json

ui_width = 30

print("Enter a name of a city for which you want to forecast")
stad = input("> ")
url = "https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/" + stad

response = requests.get(url)
response_dictionary = json.loads(response.text)


print("-" * ui_width)
print("FORECASTS".center(ui_width))
print("*" * ui_width)


forecasts = response_dictionary["forecasts"]
for forecast in forecasts:
    print(forecast["date"], forecast["forecast"])

print("-" * ui_width)