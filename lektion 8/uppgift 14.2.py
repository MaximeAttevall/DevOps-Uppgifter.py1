import os

ui_width = 30


def line(dots=False):
    if dots:
        print("******************************")
    else:
        print("------------------------------")


def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def header(header_text):
    print(header_text.center(ui_width))


def echo(text):
    print(text)


def prompt(prompt_text):
    input(prompt_text)


while True:
    line()
    header("EXEMPEL")
    line(True)
    echo("Detta är ett exempel på hur")
    echo("ett gränssnitt kan se ut.")
    line()
    header(".. vad vill du göra?")
    line()
    echo("A | Visa inköpslista")
    echo("B | Lägg till vara")
    echo("C | Ta bort vara")
    echo("X | Stäng programmet")
    line()

    prompt("Val > ")
    clear()
