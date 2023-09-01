Daniel_Radcliffe = ["man", "brun", "brun"]
Rupert_Grint = ["man", "röd", "blå"]
Emma_Watson = ["kvinna", "brun", "brun"]
Selena_Gomez = ["kvinna", "brun", "brun"]

a = input("Vad är ditt kön, man/kvinna: ").lower()
b = input("Vad har du för hårfärg: ").lower()
c = input("Vad har du för ögonfärg: ").lower()

user_properties = [a, b, c]

if user_properties in [Daniel_Radcliffe]:
    print("Dina egenskaper matchar med Daniel Radcliffe")
elif user_properties in [Rupert_Grint]:
    print("Dina egenskaper matchar med Rupert Grint")
elif user_properties in [Emma_Watson, Selena_Gomez]:
    print("Dina egenskaper matchar med Emma Watson eller Selena Gomez")
else:
    print("Du är inte lik någon skådespelare, haha!")