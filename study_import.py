""" 导入标准库 （跟随解释器一起安装时的库）"""
import sys

print(sys.version)
print(sys.platform)

""" 导入第三方库 （通过pip install安装的库）"""
# import requests
# print(requests.get("https://www.baidu.com"))
from requests import get
print(11111, get("https://www.baidu.com"))


""" 导入自己项目所写的 """
from study_str import get
print(get())
# import study_str
# print(study_str.get())

# import study_str
# print(study_str.str1)
# print(study_str.reverse_str("1234567890"))

# import study_str as ss
# print(ss.str1)

# from study_str import str1, Person
# print(str1)
# print(Person)

# from study_str import Person as MyPerson
# print(MyPerson)
