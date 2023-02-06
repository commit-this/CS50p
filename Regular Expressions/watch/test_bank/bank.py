def main():
    """ask for user to input a greeting and prints value according to seinfeld rules"""
    greeting = input("Greeting: ")
    print("$", value(greeting), sep="")


def value(greeting):
    """return value based on whether greeting starts with hello or h"""
    if greeting.strip().lower().startswith("hello"):
        return 0
    if greeting.strip().lower().startswith("h"):
        return 20
    return 100


if __name__ == "__main__":
    main()
