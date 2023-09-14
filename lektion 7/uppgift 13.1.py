import requests
import json


url = "https://4bbh01oqwj.execute-api.eu-north-1.amazonaws.com/numcheck?integer=100"
number = input("Give me a whole number: ")

response = requests.get(url, params={"integer":number}) # Följande säger att våran input "number" ska användas som "Value" i dictionaryn
response_dictionary = json.loads(response.text) # Json loads omvandlar texten vi får till en dictionary

if response_dictionary["prime"]:
    print(number, "This number is a prime number")

elif response_dictionary["even"]:
    print(number, "This is a even number not a prime number")

print("Numbers factors is", response_dictionary["factors"])
input("Press enter to try again...")