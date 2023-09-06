todos = ["städa", "handla", "plugga", "ge blod"]
todo = input("ange en todo: ")

if todo in todos:
    print("detta todo finns redan i listan :D ")
else:
    choice = input("Vill du lägga till detta (Y/N)?: ")
    if choice.lower() == "y":
        todos.append(todo)
        print(todos)
    elif choice.lower() == "n":
        print("Då lägger vi inte till något! ")
    else:
        print("detta är inte ett giltigt svar, börja om")