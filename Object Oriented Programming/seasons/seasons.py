import sys
from datetime import date
import inflect

p = inflect.engine()


def main():
    print(seasonize(input("Date of birth: ")))


def seasonize(birthday_string):
    """ find the difference between birthday input (yyyy-mm-dd) and today's date in minutes,
        return as words """
    try:
        difference = date.today() - date.fromisoformat(birthday_string)
    except ValueError:
        sys.exit("Invalid date")
    minutes = round(difference.total_seconds() / 60)
    return f"{p.number_to_words(minutes).capitalize().replace('and ', '')} minutes"


if __name__ == "__main__":
    main()
