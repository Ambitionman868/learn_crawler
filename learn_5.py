# _*_ coding:utf-8 _*_
__author__ = "Jianpan"
__date__ = "2017/11/5 下午9:41"
# 正则表达式于Cookie的使用
import re

# 原子 1

# 1.1,普通字符作为原子
# pattern = 'yue'
# string = 'http://yum.iqianyue.com'
# result = re.search(pattern, string)
# print(result)

# 1.2,非打印字符作为原子
# pattern = '\n'
# string = ''' http://yum.iqianyue.com
# http://baidu.com'''
# result = re.search(pattern, string)
# print(result)

# 1.3,通用字符作为原子
# pattern = '\w\dpython\w'
# string = 'asfs;lga3python_py'
# result = re.search(pattern, string)
# print(result)

# 1.4,原子表
# pattern1 = '\w\dpython[xyz]\w'
# pattern2 = '\w\dpython[^xyz]\w'
# pattern3 = '\w\dpython[xyz]\W'
#
# string = 'abcdefphp345pythony_py'
# result1 = re.search(pattern1, string)
# result2 = re.search(pattern2, string)
# result3 = re.search(pattern3, string)
#
# print(result1)
# print(result2)
# print(result3)

# 元字符 2

# 2.1任意匹配元字符
# pattern = '.python...'
# string = 'abcdfphp345pythony_py'
# result = re.search(pattern, string)
# print(result)

# 2.2边界限制元字符
# pattern1 = '^abd'
# pattern2 = '^abc'
# pattern3 = 'py$'
# pattern4 = 'ay$'
# string = 'abcdfphp345pythony_py'
# result1 = re.search(pattern1, string)
# result2 = re.search(pattern2, string)
# result3 = re.search(pattern3, string)
# result4 = re.search(pattern4, string)
# print(result1)
# print(result2)
# print(result3)
# print(result4)

# 2.3限定符
# pattern1 = 'py.*n'
# pattern2 = 'cd{2}'
# pattern3 = 'cd{3}'
# pattern4 = 'cd{2,}'
# string = 'abcdddfphp345pythony_py'
# result1 = re.search(pattern1, string)
# result2 = re.search(pattern2, string)
# result3 = re.search(pattern3, string)
# result4 = re.search(pattern4, string)
# print(result1)
# print(result2)
# print(result3)
# print(result4)

# 2.4模式选择符
# pattern = 'python|php'
# string = 'abcdfphp345pythony_py'
# result = re.search(pattern, string)
# print(result)

# 2.5模式单元符
pattern1 = '(cd){1,}'
pattern2 = 'cd{1,}'
string = 'abcdcdcdcdfphp345pythony_y'
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
print(result1)
print(result2)

# 模式修正 3
# 贪婪模式与懒惰模式 4
