ui_bred = 30
print(ui_bred * "*")
print("The Great Divider".center(ui_bred))
print(ui_bred * "-")

try:
    print("beräkna c för utrycket:\n a // b = c")
    print(ui_bred * "-")
    a = float(input("Skriv in ett flyttal för a: "))
    b = float(input("Skriv in ett flyttal för b: "))
    c = a / b
    print("Svaret blir: ", c)
except ValueError:
    print("Detta är inte ett flyttal,försök igen.")
except ZeroDivisionError:
    print("Division med 0 går ej,försök igen.")