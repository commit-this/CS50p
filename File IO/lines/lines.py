import sys


def main():
    """checks for invalid argv and prints number of lines of code"""
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].strip().endswith((".py")):
        sys.exit("Not a Python file")
    else:
        print(count_lines(sys.argv[1]))


def count_lines(program):
    """counts and returns lines of code in a python source file"""
    try:
        with open(program) as file:
            line_count = 0

            # loop over every row in the file, skip over blank lines and comments
            for line in file:
                if not line.strip():
                    continue
                if line.strip().startswith("#"):
                    continue
                line_count += 1

        return line_count

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
