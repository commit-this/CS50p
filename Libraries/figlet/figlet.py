import random
import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    text = input("Input: ")
    random_font = random.choice(figlet.getFonts())
    figlet.setFont(font=random_font)
    print("Output:", figlet.renderText(text))
elif len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in figlet.getFonts():
        text = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print("Output:", figlet.renderText(text))
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")