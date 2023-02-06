""" counts the number of 'um' in an input string """


import re


def main():
    print(count(input("Text: ")))


def count(s):
    """finds the length of the list returned by re.findall, using \b anchors as word boundaries"""
    return len(re.findall(r"\bum\b", s, re.I))


if __name__ == "__main__":
    main()
