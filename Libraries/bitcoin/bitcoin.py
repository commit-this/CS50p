import requests
import sys

api_url = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) == 2:
        coins = float(sys.argv[1])
        response = requests.get(api_url).json()
        price = float(response["bpi"]["USD"]["rate_float"])
        total = coins * price
        print(f"${total:,.4f}")
    else:
        sys.exit("Too many command-line arguments")

except TypeError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    sys.exit("Failed to fetch price")
