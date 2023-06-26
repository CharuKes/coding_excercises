
import sys
import requests
import json

while True:
    try:
        if len(sys.argv) != 2:
            sys.exit("Missing command-line argument")
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json?&?include=rate_float" + sys.argv[1])
        if sys.argv[1].isalpha():
            sys.exit("Command-line argument is not a number")
        else:
            b = sys.argv[1]
            o = response.json()
            for i in o["bpi"]:
                if i == "USD":
                    a = (o['bpi']["USD"]["rate_float"])
                    k = eval(f"{a} * {b}")
                    print(f"${k:,.4f}")
                    sys.exit()
    except requests.RequestException:
        break