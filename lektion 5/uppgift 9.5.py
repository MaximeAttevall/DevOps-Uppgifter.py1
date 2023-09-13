#9.5
ui_width = 30
print(".: STACKMASTER v1 .33.7 :.".center(ui_width))
print("------------------------------")

bilar = ["Mercedes", "Volvo", "Toyota"]

for bilarna in bilar:
    print("-", bilarna)

print("------------------------------")
print("| MENU |".center(ui_width))
print("------------------------------")
print(" push |  Push element to stack")
print(" pull |  Pull element from stack")
print(" exit | Exit program")
print("------------------------------")
x = input("MENU > ").lower()

if x == "push":
    add = input("Push element to stack: ")
    bilar.append(add)
    print(bilar)
elif x == "pull":
    add = input(" Pull element from stack: ")
    if add in bilar:
        bilar.remove(add)
    else:
        print(f"{add} is not in the list")
    print(bilar)
elif x == "exit":
    print("Program finished")