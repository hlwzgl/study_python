""" 不带参数的装饰器 """
def print_argument(func):

    def wrapper(num1, num2):
        print(f"func: {func.__name__}")
        print(f"num1: {num1}")
        print(f"num2: {num2}")
        return func(num1, num2)
    
    return wrapper
    

@print_argument
def add(num1, num2):
    return num1 + num2


@print_argument
def minus(num1, num2):
    return num1 - num2


@print_argument
def multiply(num1, num2):
    return num1 * num2


@print_argument
def divide(num1, num2):
    return num1 / num2


if __name__ == "__main__":
    print(add(2, 3))
    print(minus(2, 3))
    print(multiply("abc ", 3))
    print(divide(2, 3))
