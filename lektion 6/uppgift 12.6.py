import json
import os

notes = {
    "Meddelande från skolan": "Friluftsdag på tisdag",
    "Kom ihåg": "Ta bilen till verkstad",
    "Inför tentamen": "Gör alla instuderingsuppgifter"

}

if os.path.exists("notes.json"):
    with open("notes.json", "r") as f:
        notes = json.load(f)
else:
    notes = {}

ui_width = 30
while True:

    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

    print(":. ANTECKINGAR .:".center(ui_width))
    print("*" * ui_width)
    for key in notes:
        print("-", key)
    print("-" * ui_width)
    print("view | view note")
    print("add | add note")
    print("rm | remove note")
    print("exit | exit program")
    print("-" * ui_width)

    option = input(" Menu > ").lower()

    if option == "view":
        title = input("Write the title of the text you want to see > ").lower()
        if title in notes:
            print("Text - ", notes[title])
            input("Press enter to continue...")
        else:
            print("Note not found...")
    elif option == "add":
        add_notes = input("Titel >")
        add_notes2 = input("Text >")
        notes[add_notes] = add_notes2
        print("Note added...")
        input("Press enter to continue...")
    elif option == "rm":
        title = input("Write the title of the note you want to remove: ")
        del notes[title]
        print("Note deleted....")
        input("Press enter to continue...")
    elif option == "exit":
        print("Saving to notes.json...")

        with open("notes.json", "w") as f:
            json.dump(notes, f)
        break
    else:
        print("program closing.....")
