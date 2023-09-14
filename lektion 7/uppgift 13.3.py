import requests
import json

url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"

response = requests.get(url)
response_dictionary = json.loads(response.text)
artists = response_dictionary["artists"]

print("---", "ARTIST DB", "---")
for artist in artists:
    print(artist["name"])
print("----------------")
print("Select artist: ")
artist_input = input("> ").lower()
print("****************")

for artist in artists:
    if (artist["name"].lower() == artist_input):
        artist_response = requests.get(url + artist["id"])
        artist_information_dictionary = json.loads(artist_response.text)

        artist_information = artist_information_dictionary["artist"] #vi hämtar ut valuen för artist i dictionaryn

        print("Genres: ", end=" ")
        for genre in artist_information["genres"]:
            print(genre, end=", ")

        print("")
        print("Years Active:", end=" ")
        for active in artist_information["years_active"]:
            print(active,end=", ")

        print("")
        print("Members:", end=" ")
        for member in artist_information["members"]:
            print(member,end=", ")
    else:
        print(f"{artist_input} is not in the list, try again")
        break
