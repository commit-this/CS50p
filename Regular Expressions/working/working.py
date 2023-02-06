""" program to take a schedule input in 12 hour format
    and return it in 24 hour format e.g. take '9 AM to 5 PM'
    or '9:00 AM to 5:00 PM' and return '09:00 to 17:00' """


import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    """if re.search matches, print in 24 hour clock format
    if no match, raise value error"""
    if times := re.search(
        r"^([1-9][0-2]?):?([0-5][0-9])? (AM|PM) to ([1-9][0-2]?):?([0-5][0-9])? (AM|PM)$",
        s,
    ):
        first_hour, first_minutes = times.group(1), times.group(2)
        second_hour, second_minutes = times.group(4), times.group(5)
        first_ampm, second_ampm = times.group(3), times.group(6)

        first_hour, second_hour = int(first_hour), int(second_hour)
        if first_ampm == "PM":
            if first_hour < 12:
                first_hour += 12
        elif first_ampm == "AM" and first_hour == 12:
            first_hour = 0
        if second_ampm == "PM":
            if second_hour < 12:
                second_hour += 12
        elif second_ampm == "AM" and second_hour == 12:
            second_hour = 0

        if not first_minutes and not second_minutes:
            return f"{first_hour:02}:00 to {second_hour:02}:00"
        return f"{first_hour:02}:{first_minutes} to {second_hour:02}:{second_minutes}"
    raise ValueError


if __name__ == "__main__":
    main()
