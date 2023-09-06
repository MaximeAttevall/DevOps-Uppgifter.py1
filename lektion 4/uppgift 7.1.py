import os

POST_1 = ""
POST_2 = ""
POST_3 = ""
while True:
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
print("Detta är en anslags tavla där du kan ändra informationen")
print (".: basicBILLBOARD :.")
print ("********************")
print ("P1:", POST_1 )
print ("P2:", POST_2 )
print ("P3:", POST_3 )
print ("--------------------")
print ("c| Ändra post")
print ("e | Stäng program")
print ("--------------------")
print("meny >")
command = input(": ")
    if command == c:
        command_2 = input("P1", "P2", "P3", "vilken post vill du ändra: ")
    elif command_2 == "P1":
        input("Varsågod att ändra: ") = P1 

# [ ] 4. Utför operationer för inmatat kommando
# [X] 5. Pausa exekvering
input ("Tryck enter fär att fortsätta... ")
# [X] 6. Gå till 1