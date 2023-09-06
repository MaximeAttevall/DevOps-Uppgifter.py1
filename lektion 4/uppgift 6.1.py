#Vi ska göra ett program som räknar den bokstaven vi anger och hur många gånger den framkommer.
text = input("Skriv en mening: ").lower()
target_char = input("skriv en bokstav i meningen: ").lower()
count = 0

#för char i texten > om char i target_char är identiska så räkna hur månag gånger char används
for char in text:
    if char == target_char:
        count += 1

print("Detta är hur många gånger", target_char.upper(), "förekommer", count)


"""
count = text.count(target_char)
print("Detta är hur många gånger", target_char.upper(), "förekommer", count)
"""