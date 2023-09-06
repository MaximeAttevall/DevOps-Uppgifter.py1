#Allt under är för synsskull, sätter en bred på rad 2 som säger ui_bred = 30 "platser" "rader" "steg"
ui_bred = 30
print(ui_bred * "*")
print(":.Mathlete v2.0.:".center(ui_bred))
print(ui_bred * "-")

inmatade_tal = [] #detta sätter en tom lista för variabeln


while True: #startar loopen
    try: # Detta är kommande för vilken del av koden "except" ska gälla för
        inmatat_tal = input("mata in ett heltal: ") #variabel för de siffror ellerkaraktärer användare matar in
        if inmatat_tal.lower() == "exit": # ifall variabeln är = exit, så avslutas loopen och programmet
            break
        inmatat_tal = int(inmatat_tal) # Detta sätter så att variabeln är definerad som en siffra nu "matematisk" siffra
        inmatade_tal.append(inmatat_tal) # Append sätter in alla mattade talen i variabeln i den tomma listan vi satt ovan "inmatade_tal", jag tycker det ser lite tvärtom ut men så fungerar det.
    except ValueError:
        print("FEL Ogiltigt nummer") #detta felmeddelande kommer fram ifall någon skriver in en karaktärer och inte en siffra

print(ui_bred * "-")
print("Summa: ", sum(inmatade_tal)) # Detta räknadar ut summan av alla inmatade tal i listan
print("Medelvärdet", sum(inmatade_tal)/len(inmatade_tal))# detta räknar ut medelvärdet av alla tal i listan.
print("Kardinalitet: ", len(inmatade_tal)) # Detta räknade ut antalet inmatade tal i listan, hur många gånger.

#då Vet vi att Sum / len, är summan av alla tal delat på antalet tal vi skrivit in = medelvärdet.