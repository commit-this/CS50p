import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    """ parses HTML for a youtube embed link within an iframe tag and returns shortened vid URL """
    if match := re.search(r"<iframe.+youtube.com/embed/(\w+)", s, re.IGNORECASE):
        return f"https://youtu.be/{match.group(1)}"
    return None

if __name__ == "__main__":
    main()
