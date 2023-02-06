""" program to count lines of code
    in a python source file
    excluding comments, docstrings, and empty lines
    run on command line with "python lines.py {source file}" """


import sys


def main():
    valid_arguments()
    print(count_lines(sys.argv[1]))


def valid_arguments():
    """ checks for invalid command line arguments """
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].strip().endswith((".py")):
        sys.exit("Not a Python file")


def count_lines(source):
    """ returns # of lines of code in a python source file """
    try:
        with open(source) as file:
            line_count = 0
            docstring_count = 0
            docstring_tags = tuple(["'''", "\"\"\""])

            # loop over every row of code in the file
            # skip over blank lines and docstrings and comments
            # else count every line that has text

            for line in file:
                if not line.strip():
                    continue
                if line.strip().startswith("#"):
                    continue
                if len(line.strip()) == 3:
                    if line.strip().startswith(docstring_tags):
                        docstring_count += 1
                elif len(line.strip()) > 3:
                    if line.strip().startswith(docstring_tags):
                        docstring_count += 1
                    if line.strip().endswith(docstring_tags):
                        docstring_count += 1
                if docstring_count % 2 != 0:
                    continue
                line_count += 1

        return line_count

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
