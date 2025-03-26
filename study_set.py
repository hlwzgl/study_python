""" 定义和初始化 """
set_1 = {1, 2, 2, "a", "bc", "洪亮"}
set_2 = set()
set_3 = set({1, 2, "a"})

""" 增 """
set_3.add("曹文")

""" 删 """
set_1.remove(2)
set_1.pop()
set_1.pop()
set_1.clear()

""" 改 """
set_3.update({1, 2, 3})

""" 查 """
set_31 = set_3.copy()

print("end")
