import random


def main():
    # counter variables to keep track of questions asked and score
    questions = 0
    score = 10

    level = get_level()

    # while loop asks 10 addition questions, then breaks loop and prints score
    while True:
        # counter variable to track incorrect answers
        eee = 1
        x = generate_integer(level)
        y = generate_integer(level)
        questions += 1
        if questions > 10:
            break
        print(x, "+", y, "=", end=" ")
        answer = int(input())

        if answer == x + y:
            continue
        else:
            # if question answered incorrectly, inner while loop gives 2 additional chances to answer before showing the correct answer, decrementing score and asking another question
            while True:
                if eee == 3:
                    score -= 1
                    print(x, "+", y, "=", x + y)
                    break
                else:
                    print("EEE")
                    eee += 1
                    print(x, "+", y, "=", end=" ")
                    answer = int(input())
                    if answer == x + y:
                        break

    print(f"Score: {score}")


# get_level gets level of difficulty from the user and generate_integer generates random integer based on level


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                raise ValueError
            return level
        except (ValueError, TypeError):
            pass


def generate_integer(level):
    levels = {
        1: [0, 10],
        2: [10, 100],
        3: [100, 1000],
    }
    return random.randrange(levels[level][0], levels[level][1])

    # if level == 1:
    #     return random.randrange(0, 10)
    # elif level == 2:
    #     return random.randrange(10, 100)
    # elif level == 3:
    #     return random.randrange(100, 1000)


if __name__ == "__main__":
    main()
