print("KORVKOLLEN 1.0.1")
#Input hur många personer villa ha olika korvar
two_vanlig_korv = input("Hur många personer som vill ha 2st vanliga korvar?")
tre_vanlig_korv = input("Hur många personer som vill ha 3st vanliga korvar?")
two_vegan_korv = input ("Hur många personer som vill ha 2st veganska korvar?")
tre_vegan_korv = input ("Hur många personer som vill ha 3st veganska korvar?")

#Pris
vanlig_korv_packning_pris = 20.95
vegan_korv_packning_pris = 34.95
dricka_pris = 13.95

#Beräkna hur många korvar det blir för våra valiga,veganska och drickor
antal_vanlig_korv = int(two_vanlig_korv)*2 + int(tre_vanlig_korv)*3
antal_vegan_korv = int(two_vegan_korv)*2 + int(tre_vegan_korv)*3
antal_drickor = int(two_vanlig_korv) + int(tre_vanlig_korv) + int(two_vegan_korv) + int(tre_vegan_korv)

#Beräkna antalet förpackningar, som behövs köpas in
#Delar antalet personer med antalet korvar i en förpakcning så vet vi hur många förpacknigar vi behöver, sean avrundar vi det uppåt(för mycket korvar > för lite korvar)
antal_vanliga_förpackningar_att_köpa = round((int(antal_vanlig_korv) / 8 + 0.5))
antal_veganska_förpackningar_att_köpa = round((int(antal_vegan_korv) / 4 + 0.5))
print("--------INKÖPNINGSLISTA--------")

#printar ut hur många förpackningar + drickor
print("Vanlig korv: ", antal_vanliga_förpackningar_att_köpa, "förpackningar")
print("vegansk korv: ", antal_veganska_förpackningar_att_köpa, "förpackningar")
print("Dryck", antal_drickor)

#sedan tar vi priser per förpackning + dricka gånger antalet, sedan slår ihop det.
a = (vanlig_korv_packning_pris) * (antal_vanliga_förpackningar_att_köpa)
b = (vegan_korv_packning_pris) * (antal_veganska_förpackningar_att_köpa)
c = (dricka_pris) * (antal_drickor)
total_pris = a + b + c

print(total_pris, "SEK")