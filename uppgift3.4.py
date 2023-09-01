a = input("skriv in ett land i norden eller i storbritanien: ")

b = ["sverige", "finland", "norge", "danmark", "island"]


if a.lower() in b:
    print("Detta land tillhör Norden")
elif a.lower() in ["england", "wales", "skottland", "nordirland"]:
    print("Detta land tillhör Storbritannien")
else:
    print("Detta är inte ett land som tillhör Norden eller Storbritannien")
