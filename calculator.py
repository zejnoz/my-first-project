def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


if __name__ == "__main__":
    print(add(2, 2))
    print(sub(10, 8))
    print(multiply(52, 10))
    print(divide(10, 7))
