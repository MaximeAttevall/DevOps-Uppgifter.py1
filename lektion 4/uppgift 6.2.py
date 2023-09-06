ui_width = 30
#Sätt variabel på alla konsonanter
sentence = input("Skriv en mening på svenska: ")
consonant = "bcdfghjklmnpqrstvwxz"

#Sätt en tom variabel som en sträng
result = ""
#för char i meningen, om char finns i konsonanter > ta tommma result och plussa på char + "o" + char inuti sentence.
#annars ifall konsonant ej finns, körs ej if statment.
for character in sentence:
    if character.lower() in consonant:
        result += character + "o" + character

print("Robber Translate")
print(ui_width * "-")
print("Svenska: ", sentence)
print("Rövarspråket: ", result)