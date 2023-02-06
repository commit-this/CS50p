answer = input("What is the Answer to the Great Question of Life, The Universe, and Everything? ")
if answer.strip() == "42" or answer.strip().lower() == "forty two" or answer.strip().lower() == "forty-two":
    print("Yes")
else:
    print("No")