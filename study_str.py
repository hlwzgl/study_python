""" 定义和初始化 """
str_1 = ""
str_2 = "HELLO"
str_3 = str()
str_4 = str("Hello")
str_5 = f"{str_2} WORLD"
str_6 = f"{str_2 + str_4} world"
str_7 = f"{str_2 + ' a'} world"
str_8 = '''
abcde
hijkl
'''
str_9 = """
adfsdf
dssfdsaf
"""

""" 增 """
str_21 = " ".join("1234567890")
str_22 = "hello {}, {}".format("abcd", "hijk")
str_23 = "hello {}, {}"

""" 删 """
str_41 = str_4.removeprefix("H")
str_42 = str_4.removesuffix("lo")
str_44 = str_4.lstrip("H")
str_43 = str_4.strip()
str_44 = str_4.lstrip("H")
str_45 = str_4.rstrip("o")


""" 改 """
str_51 = str_5.replace("world", "china")
str_52 = str_5.title()
str_53 = str_5.lower()
str_54 = str_5.upper()
str_55 = str_5.capitalize()

""" 查 """
str_61 = str_6.find("O")
str_62 = str_6.index("O")
str_63 = str_6[12]
print("end")
