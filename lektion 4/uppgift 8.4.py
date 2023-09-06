todos = ["städa", "handla", "plugga", "ge blod"]

todo = input("Ta bort ett värde: ")

if todo in todos:
    todos.remove(todo)
    print(todos)
else:
    print("angivna ordet finns ej i listan")