#7.1
import os

POST_1 = ""
POST_2 = ""
POST_3 = ""

while True:
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    print(".: basicBILLBOARD :.")
    print("********************")
    print("P1:", POST_1 )
    print("P2:", POST_2 )
    print("P3:", POST_3 )
    print("--------------------")
    print("c | Ändra post")
    print("e | Stäng program")
    print("--------------------")

    user_input = input("meny >  ").lower()
    if user_input == "c":
        post_input = input("svara med vilken post du vill ändra på? (1, 2, 3): ")
        if post_input == "1":
            POST_1 = input("Vad är din post: ")
        elif post_input == "2":
            POST_2 = input("Vad är din post: ")
        elif post_input == "3":
            POST_3 = input("Vad är din post: ")
    elif user_input == "e":
        print("Avslutar program")
        break