import validators


def main():
    print(validate(input("What's your email address? ")))


def validate(email_address):
    if validators.email(email_address):
        return "Valid"
    return "Invalid"


if __name__ == "__main__":
    main()
