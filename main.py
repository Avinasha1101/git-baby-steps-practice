from calculator import Calculator


def main():
    calc = Calculator()
    a = 10
    b = 4

    print(f"{a} + {b} = {calc.add(a, b)}")
    print(f"{a} - {b} = {calc.subtract(a, b)}")
    print(f"{a} * {b} = {calc.multiply(a, b)}")
    print(f"{a} / {b} = {calc.divide(a, b)}")


if __name__ == "__main__":
    main()