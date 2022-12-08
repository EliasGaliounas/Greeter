print("executing greeter.py, __name__ is", __name__)
import colorama  # used for creating coloured text


def greet(personal, family, title="", polite=False):
    greeting = "How do you do, " if polite else "Hey, "
    greeting = colorama.Back.BLACK + colorama.Fore.YELLOW + greeting
    if title:
        greeting += colorama.Back.BLUE + colorama.Fore.WHITE + title + " "

    greeting += (
        colorama.Back.WHITE
        + colorama.Style.BRIGHT
        + colorama.Fore.RED
        + personal
        + " "
        + family
    )
    return greeting


# def greet(personal, family):
#     return "Hey, " + personal + " " + family


if __name__ == "__main__":
    print(greet("Laura", "Greeter"))