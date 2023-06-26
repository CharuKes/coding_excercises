import pyfiglet
from pyfiglet import Figlet
import sys
import random
figlet = Figlet()
font_names = pyfiglet.Figlet().getFonts()
selected_font = random.choice(font_names)

if len(sys.argv) == 1:
    user_word = input("What would you like to print:")
    banner = pyfiglet.figlet_format(f"{user_word}", font=selected_font)
    print(f"{banner}", sys.argv[0])

elif len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--f':
        if sys.argv[2] in font_names:
            user_word = input("What would you like to print:")
            banner = pyfiglet.figlet_format(f"{user_word}", font=sys.argv[2])
            print(banner)
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
