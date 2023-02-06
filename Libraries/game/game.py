import random

# use 2 while true loops, first loop will ask user for level and generate random integer, second loop will check the user's guess

while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            continue
        answer = random.randrange(1, level + 1)
        break
    except (TypeError, ValueError):
        pass

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            continue
        elif guess < answer:
            print("Too small!")
        elif guess > answer:
            print("Too large!")
        else:
            print("Just right!")
            break
    except (TypeError, ValueError):
        pass
