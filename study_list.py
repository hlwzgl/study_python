""" 定义和初始化 """
list_1 = []   # list()
list_2 = [1, 3, "a", "bc", list_1] # list([1, 3, "a", "bc", list_1])

""" 增 """
list_1.append("洪亮")
list_1.insert(0, "曹文")
list_1.extend("abc")
list_1.extend(["abc"])
list_1.extend(("def"))


""" 删 """
list_2.pop()
list_2.pop(0)
list_2.remove("bc")
list_2.clear()


""" 改 """
list_1[0] = "洪亮"
list_1.reverse()
list_1.sort()


""" 查  """
a = list_1[0]
b = list_1.index("洪亮")
c = list_1.count("j")
d = list_1.copy()

# list_1[0] = "==="
# d [0] = "**"

""" 魔术方法 """
e = list_1 + ["Jiayou"]
f = list_1 == d
g = list_1.__len__()
h = len(list_1)

print("end")
