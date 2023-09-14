import requests
import json

for number in range(2,100):
    url = "https://4bbh01oqwj.execute-api.eu-north-1.amazonaws.com/numcheck?integer=100"
    number = input("Give me a whole number: ")

    response = requests.get(url, params={"integer":number})
    response_dictionary = json.loads(response.text)
    if json.loads(response.text)["prime"]:
        print(number, "This number is a prime number")
        print("Numbers factors is", response_dictionary["factors"])
        input("Press enter to try again...")
    elif json.loads(response.text)["even"]:
        print(number, "This is a even number not a prime number")
        print("Numbers factors is", response_dictionary["factors"])
        input("Press enter to try again...")