import json
import os

notes = {
    "Testing":" Of the test",
    "Crazy":"Hamburgaah"
}

file_read = open("notes.json", "r")

if os.path.exists("notes.json"):
    notes = json.load(file_read)
file_read.close()

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
    print("view \t| view note")
    print("add \t| add note")
    print("rm  \t| remove note")
    print("exit \t| exit program")
    print("-" * ui_width)

    option = input(" Menu > ").lower()

    if option == "view":
        for title in notes:
            print(title,"-", notes[title])

        input("Press enter to continue...")

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
        break

    elif option == "clear notes":
        notes.clear()
    else:
        print("program closing.....")

file_write = open("notes.json", "w")
json.dump(notes, file_write)
file_write.close()