while True:
    try:
        x, y = input("Fraction: ").split("/")
        percent = round((int(x) / int(y)) * 100)
        if int(x) > int(y):
            continue
        elif percent >= 99:
            print("F")
        elif percent <= 1:
            print("E")
        else:
            print(percent, "%", sep="")
        break
    except (ValueError, ZeroDivisionError):
        pass