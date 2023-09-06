#Ej klar


print("NUMANALYZER")
print("v1 .33.7")
start_tal = 1000000000
nuvarande_minsta_tal = start_tal

while True:
    inmatat_tal = int(input("mata in ett tal: "))

    if inmatat_tal < 0:
        break
    if inmatat_tal < nuvarande_minsta_tal:
        nuvarande_minsta_tal = inmatat_tal

print("nuvarande_minsta_talet är", nuvarande_minsta_tal )