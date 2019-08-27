# _*_ coding=utf-8 _*_

import pandas as pd

"""Series——一维数组对象：
    由一组数据和一组与之相关的数据标签（索引）组成    
    比较像列表和字典的结合体
"""

"""-----创建Series-----"""
# 创建一个数组，并设置标签，可以使用标签和索引访问
arr = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(arr)
print(arr[0], arr['a'])

# 创建一个数组,可以使用标签和索引访问
arr_dic = pd.Series({'a': 1, 'b': 2})
print(arr_dic[1])
print(arr_dic)

# 创建一个元素全为0的数组
arr_zero = pd.Series(0, index=['a', 'b', 'c', 'd'])
print(arr_zero)

"""-----使用Series-----"""
# 　具有ndarry的属性,以及支持字典的特性
arr_dict = pd.Series({'a': 2, 'b': 3})  # 从字典创建

# in运算
print('a' in arr_dict)

# 键索引,取多个标签，标签切片
print(arr[['a', 'b']])
print(arr['a':'c'])
