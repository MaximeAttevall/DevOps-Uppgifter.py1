age = input("hej hur gammal är du?")
if int(age) < 18:
    print("du får dricka om " + str(18 - int(age)) + "år! ")
elif age == 18:
    print("du får dricka iår")
else:
    print("Du får redan dricka ")