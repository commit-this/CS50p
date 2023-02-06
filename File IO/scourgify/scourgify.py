"""
program to clean up names from a csv file and write to a new csv file
names stored as "Last, First" will be split and written as "First", "Last"
"""


import sys
import csv


# buffer list will store cleaned up dicts read from initial csv
buffer = []


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        scourgify(sys.argv[1])
        output(sys.argv[2])


def scourgify(before_csv):
    """reads csv file, splitting names into first and last and adding each row to buffer"""
    try:
        with open(before_csv) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(",")
                first = first.strip()
                buffer.append({"first": first, "last": last, "house": row["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read {before_csv}")


def output(after_csv):
    """writes buffer to new csv file"""
    with open(after_csv, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in buffer:
            writer.writerow(
                {"first": row["first"], "last": row["last"], "house": row["house"]}
            )


if __name__ == "__main__":
    main()
