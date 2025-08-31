def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    assert b != 0
    return a / b

if __name__ == "__main__":
    add(2, 3)
    subtract(5, 3)
    multiply(4, 6)
    divide(8, 2)
