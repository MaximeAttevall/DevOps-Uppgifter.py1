# omvandla miles to kilometrar och tvärtom

choice = input("Do you want to convert miles to kilometers (m) or kilometers to miles (k)? ")


def miles_to_km(miles):
    return miles * 1.609344


def km_to_miles(km):
    return km / 1.609344


if choice == "m":
    miles = float(input("Enter the number of miles: "))
    kilometers = miles_to_km(miles)
    print(f"{miles} miles is equal to {kilometers} kilometers.")
elif choice == "k":
    kilometers = float(input("Enter the number of kilometers: "))
    miles = km_to_miles(kilometers)
    print(f"{kilometers} kilometers is equal to {miles} miles.")
else:
    print("Invalid choice.")
