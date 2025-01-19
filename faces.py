def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")


def main():
    str = input("Tell me how you're feeling... ")
    print(convert(str))


main()
