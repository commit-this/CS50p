menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# define variable to keep track of order total outside of the loop so it does not get reset
total = 0
while True:
    try:
        order = input("Item: ").title()
        if order in menu:
            total += menu[order]
            print(f"Total: ${total:.2f}")
    except KeyError:
        pass
    # EOF exception catches a user ctrl-d escape from the program and prints a new line
    except EOFError:
        print()
        break