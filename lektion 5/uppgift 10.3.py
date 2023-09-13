#uppgift 10.3
import os

file_name = "textfil.txt"
if os.path.exists(file_name) == False:
    open(file_name, 'x')

while True:
    ui_width = 30
    print("-" * ui_width)
    text_file = open(file_name, 'r')
    print(text_file.read())
    print("-" * ui_width)
    print("| C |  Change sign message")
    print("| E |  Exit program")
    print("-" * ui_width)

    user_input = input("Enter COMMAND: ").lower()
    if user_input == "c":
        if os.path.exists(file_name):
            text_file = open(file_name, 'w')
            sign_input = input("> ")
            text_file.write(sign_input)
            text_file.close()
    elif user_input == "e":
        print("PROGRAM SHUTDOWN")
        break
    elif user_input == "x":
        file_name = input("what is your filename?: ")
        if os.path.exists(file_name) == False:
            open(file_name, 'x')