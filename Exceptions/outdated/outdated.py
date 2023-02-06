months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    try:
        date = input("Date: ")
        # check what date format was input by checking if the first character is alphabetical
        if date[0].isalpha():
            month, day, year = date.title().split(" ")
            if day[1] != "," or day[2] != ",":
                continue
            elif month in months:
                # month will be given a value of index + 1 because of zero indexing
                month = months.index(month) + 1
                day, year = int(day.strip(",")), int(year)
                if day > 31:
                    continue
                print(f"{year}-{month:02}-{day:02}")
                break
        else:
            month, day, year = date.split("/")
            month, day, year = int(month), int(day), int(year)
            if month > 12 or month < 1:
                continue
            elif day > 31:
                continue
            print(f"{year}-{month:02}-{day:02}")
            break

    except (ValueError, IndexError, TypeError):
        pass
