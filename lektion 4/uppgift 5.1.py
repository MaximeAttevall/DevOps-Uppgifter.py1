while True:
    try:
        heltal = int(input("mata in ett heltal: "))
        print("Resultat", heltal * 2)
        break
    except ValueError:
        print("Fel, måste vara ett heltal, försök igen")
