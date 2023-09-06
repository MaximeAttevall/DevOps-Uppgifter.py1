
sentence = input("skriv en mening: ")
reversed_sentence = sentence[::-1]

if reversed_sentence == sentence:
        print("Detta är en palindrom", reversed_sentence, end="")
else:
    print("Detta är inte en palindrom: ", sentence)
