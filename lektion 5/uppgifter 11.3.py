#11.3
import json
import os

file_name = "file.json"

if os.path.exists(file_name):
    with open(file_name, "r") as f:
        nummer = json.load(f)
else:
    nummer = []

summa = sum(nummer)

while True:

    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

    ui_width = 30
    print(".: intMEMERIZER :.".center(ui_width))
    print("*" * ui_width)
    print("-" * ui_width)
    print("summa: ", summa)
    print("-" * ui_width)
    print("- Mata in heltal")
    print("- 0 stänger scriptet")
    print("-" * ui_width)

    rensa = input("önskar du rensa listan ja/nej: ").lower()
    if rensa == "ja":
        nummer.clear()
        with open(file_name, "w") as f:
            json.dump(nummer, f)
    elif rensa == "nej":
        print("listan fortsätter...")
    else:
        print("skriv in ja eller nej och försök igen")
        continue

    try:
        value = int(input("> "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue

    nummer.append(value)
    summa += value

    if value == 0:
        break

    with open(file_name, "w") as f:
        json.dump(nummer, f)