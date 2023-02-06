import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].strip().endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        print(tablify(sys.argv[1]))


def tablify(csv_file):
    """takes a csv and uses tabulate to return a pretty table, using first row as headers"""
    menu = []

    try:
        with open(csv_file) as file:
            reader = csv.reader(file)
            # loop over each row, appending it as a list to the menu list
            for row in reader:
                menu.append(row)
            return tabulate(menu, headers="firstrow", tablefmt="grid")

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
