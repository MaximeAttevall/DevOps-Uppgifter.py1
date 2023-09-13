import json

random_stuff = [13378, 13.37, "Aåh Yää!"]
with open("file.txt", "w") as jsonfile:
    random_stuff = json.dumps(random_stuff)
    jsonfile.write(random_stuff)

    print(random_stuff)

