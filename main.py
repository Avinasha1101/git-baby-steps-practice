from calculator import add, subtract


def main():
    a = 10
    b = 4

    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")


if __name__ == "__main__":
    main()