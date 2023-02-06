def convert(s):
    return s.replace(":(", "🙁").replace(":)", "🙂")

def main():
    answer = convert(input("How do you do: "))
    print(answer)

main()