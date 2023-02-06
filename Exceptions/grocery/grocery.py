groceries = {}

while True:
    try:
        item = input().upper()
        groceries[item] = groceries.get(item, 0) + 1
        # populate dictionary with key value pairs. initialize value to 1 if not already existing, else add 1
        # if item in groceries:
        #     groceries[item] += 1
        # else:
        #     groceries[item] = 1
    except KeyError:
        pass
    except EOFError:
        # sort dictionary alphabetically by keys with sorted function and items method
        # groceries = dict(sorted(groceries.items()))
        for item in sorted(groceries.keys()):
            print(groceries[item], item)
        break