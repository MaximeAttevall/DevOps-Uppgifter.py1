a = int(input("age ett tal: "))
b = int(input("ange ännu ett tal: "))
c = int(input ("ange ett sista tal: "))

if a >= b and a >= c:
    print("detta är det största talet", a)
if b >= a and b >= c:
    print("detta är det största talet", b)
elif c >= a and c >= b:
    print("detta är det största talet", c)