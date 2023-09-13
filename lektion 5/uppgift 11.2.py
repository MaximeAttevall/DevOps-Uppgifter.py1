#11.2
import json

with open("file.json", "w", encoding="utf-8") as f:
    my_chars = ["abc", "\u00e5\u00e4\u00f6", "123"]
    json_str = json.dumps(my_chars, ensure_ascii=False)
    f.write(json_str)

    for x in my_chars:
        print(x)



"""encoding="utf-8""" #följande behövs eftersom åöä finns i json strängen
"""ensure_ascii=False""" #Samma här