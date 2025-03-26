pi = 3.1415926

""" 函数定义 """
def add(num1, num2):
    print(f"num1: {num1}")
    print(f"num2: {num2}")
    return num1 + num2


""" 函数调用 """
# result = add(2, 3)
# print(f"result: {result}")

# result = add("b", "c")
# print(f"result: {result}")

# print("end")

if __name__ == "__main__":
    result = add(2, 3)
    print(f"result: {result}")

    result = add("b", "c")
    print(f"result: {result}")

    print("end")
