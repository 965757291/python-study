"""
输入年份判断是不是闰年
可以被4整除 如果是100的倍数 那必须被400整除
"""
year = int(input('请输入年份：'))
# 如果代码太长写成一行不便于阅读 可以使用\对代码进行折行
is_flag = (year % 400 == 0) or \
          (year % 100 != 0 and year % 4 == 0)
print(is_flag)