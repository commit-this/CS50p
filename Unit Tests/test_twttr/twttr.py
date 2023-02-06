def main():
    """asks user for string input and prints the input with all vowels removed"""
    text = input("Input: ")
    print("Output:", shorten(text))


def shorten(word):
    """takes a word and returns the word with vowels removed"""
    for char in word:
        if char.lower() in ["a", "e", "i", "o", "u"]:
            word = word.replace(char, "")
    return word


if __name__ == "__main__":
    main()
