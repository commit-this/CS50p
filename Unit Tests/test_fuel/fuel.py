"""
Program to take a fraction from user input, and print it as a percentage to simulate a fuel gauge
"""


def main():
    while True:
        try:
            percentage = convert(input("Fraction: "))
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError, TypeError):
            pass


def convert(fraction):
    """take a fraction and convert it to percentage as rounded int out of 100"""
    x, y = fraction.split("/")
    if int(x) > int(y):
        raise ValueError
    return round((int(x) / int(y)) * 100)


def gauge(percentage):
    """returns string for full, empty, or percentage of tank that is full"""
    if percentage >= 99:
        return "F"
    if percentage <= 1:
        return "E"
    return f"{percentage}%"


if __name__ == "__main__":
    main()
