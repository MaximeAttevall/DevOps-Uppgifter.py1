a = input("Vad är ditt namn?: ")
b = int(input("vad är din ålder?: "))

if b == 1:
    print("Hej", a)
    print("Vi rekommenderar 14tim sömn")
elif b == 2:   
    print("Hej", a)
    print("Vi rekommenderar 13tim sömn")
elif b == 3:   
    print("Hej", a)
    print("Vi rekommenderar 12tim sömn")
elif b == 4:
    print("Hej", a)
    print("Vi rekommenderar 11.5tim sömn")
elif b == 5 or b == 6:
    print("Hej", a)
    print("Vi rekommenderar 11tim sömn")
elif b == 7:
    print("Hej", a)
    print("Vi rekommenderar 10.5tim sömn")
elif b >= 8 and b <= 10:
    print("Hej", a)
    print("Vi rekommenderar 10tim sömn")
elif b == 11:
    print("Hej", a)
    print("vi rekommenderar 9.5tim sömn")
elif b >= 12 and b <= 15:
    print("Hej", a)
    print("Vi rekommenderar 9tim sömn")
elif b == 16:
    print("Hej", a)
    print("Vi rekommenderar 8.5tim sömn")
elif b == 17:    
    print("Hej", a)
    print("Virekommenderar 8tim sömn")  
else:
    print("Hej", a)
    print("Vi rekommenderar 8tim sömn")   