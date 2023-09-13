notes = {
    "Meddelande från skolan": "Friluftsdag på tisdag",
    "Kom ihåg": "Ta bilen till verkstad",
    "Inför tentamen": "Gör alla instuderingsuppgifter"

}

print("Lägg till artikel: ")
add_notes = input("titel > ")
add_notes2 = input("text > ")

notes[add_notes] = add_notes2

for key in notes:
    print("----")
    print("Titel: ", key )
    print("Text: ", notes[key])
