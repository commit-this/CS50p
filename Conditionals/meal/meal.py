def main():
    time = convert(input("What time is it: "))

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    if "m" in time.lower():
        num, suffix = time.split(" ")
        hours, minutes = num.split(":")
        if suffix.lower() == "am" or suffix.lower() == "a.m.":
            hours = float(hours)
        elif suffix.lower() == "pm" or suffix.lower() == "p.m.":
            hours = float(hours)
            if hours != 12:
                hours = hours + 12
        hourFraction = float(minutes) / 60
        return hours + hourFraction
    else:
        hours, minutes = time.split(":")
        hours = float(hours)
        hourFraction = float(minutes) / 60
        return hours + hourFraction

if __name__ == "__main__":
    main()


'''
original solution(s)
'''
# def main():
#     time = convert(input("What time is it: "))

#     if 7 <= time <= 8:
#         print("breakfast time")
#     elif 12 <= time <= 13:
#         print("lunch time")
#     elif 18 <= time <= 19:
#         print("dinner time")

# def convert(time):
#     hours, minutes = time.split(":")
#     hours = float(hours)
#     hourFraction = float(minutes) / 60
#     return hours + hourFraction

# if __name__ == "__main__":
#     main()



# def main():
#     time = convert(input("What time is it: "))

#     if 7 <= time <= 8:
#         print("breakfast time")
#     elif 12 <= time <= 13:
#         print("lunch time")
#     elif 18 <= time <= 19:
#         print("dinner time")

# def convert(time):
#     num, suffix = time.split(" ")
#     hours, minutes = num.split(":")
#     if suffix.lower() == "am" or suffix.lower() == "a.m.":
#         hours = float(hours)
#     elif suffix.lower() == "pm" or suffix.lower() == "p.m.":
#         hours = float(hours)
#         if hours != 12:
#             hours = hours + 12
#     hourFraction = float(minutes) / 60
#     return hours + hourFraction

# if __name__ == "__main__":
#     main()