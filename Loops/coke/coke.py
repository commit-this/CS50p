price = owed = 50
paid = 0

while True:
    print(f"Amount due: {owed}")
    coin = int(input("Insert coin: "))
    if coin in [5, 10, 25]:
        paid += coin
        if paid < owed:
            owed = price - paid
        elif paid >= price:
            owed = price - paid
            print(f"Change owed: {-1 * owed}")
            break