import pyfiglet

def fancyText(text):
    art = pyfiglet.figlet_format(text)
    return art

print(fancyText("Your computer is hacked !!!"))