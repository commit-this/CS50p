def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """function returns false if plate string s is invalid"""
    # check that plate is alphanumeric
    if not s.isalnum():
        return False
    # check that first two chars are alphabet
    if not s[0:2].isalpha():
        return False
    # check length requirement
    if len(s) < 2 or len(s) > 6:
        return False
    # check for invalid numbers by counting number of digits and using negative indices
    nums = len([c for c in s if c.isdigit()])
    if nums:
        if s[-nums] == "0" or not s[-nums:].isdigit:
            return False

    return True

if __name__ == "__main__":
    main()
