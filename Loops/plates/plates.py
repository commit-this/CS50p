def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s.isalnum():
        return False
    elif not s[0:2].isalpha():
        return False
    elif len(s) < 2 or len(s) > 6:
        return False
    for c in range(len(s)-1):
        if s[c] == "0":
            return False
        elif s[c].isdigit() and s[c+1].isalpha():
            return False


    return True


main()
