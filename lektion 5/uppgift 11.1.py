import json

random_stuff = [13378, 13.37, "Aåh Yää!"]
with open ("file.txt", "w") as f:
    random_stuff = json.dumps(random_stuff)
    f.write(random_stuff)

    print(random_stuff)

