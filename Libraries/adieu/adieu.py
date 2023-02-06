import inflect

p = inflect.engine()
names = []

while True:
    try:
        adieu = "Adieu, adieu, to"
        name = input()
        names.append(name)
    except EOFError:
        print(adieu, p.join(names))
        break
    except (TypeError, IndexError, ValueError):
        pass