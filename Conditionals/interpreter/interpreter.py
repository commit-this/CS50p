x, y, z = input("Expression: ").split(" ")
x = float(x)
z = float(z)

match y:
    case "-":
        print(f"{(x - z):.1f}")
    case "+":
        print(f"{(x + z):.1f}")
    case "*":
        print(f"{(x * z):.1f}")
    case "/":
        print(f"{(x / z):.1f}")
    case _:
        print("Unknown operation")

# if y == "-":
#     print(f"{(x - z):.1f}")
# elif y == "+":
#     print(f"{(x + z):.1f}")
# elif y == "*":
#     print(f"{(x * z):.1f}")
# elif y == "/":
#     print(f"{(x / z):.1f}")