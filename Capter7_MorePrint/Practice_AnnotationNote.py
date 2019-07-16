'''
@message: 习题训练
            巩固练习：1.添加注释

@Author: Raynor.shang
@since: 2019-07-16 07:57:58
@lastTime: 2019-07-16 08:24:36
@LastAuthor: Raynor.shang
'''

# 打印字符串
print("Mary had a little lamb.")
# 使用format方法为字符串注入变量，然后进行打印
print("Its fleece was white as {}.".format('snow'))
# 打印字符串
print("And everywhere that Mary went.")
# 打印重复10次的字符串
print("." * 10)     # what'd that do?   print '.' 10 times.

# 定义字符串变量
end1 = "C"
# 定义字符串变量
end2 = "h"
# 定义字符串变量
end3 = "e"
# 定义字符串变量
end4 = "e"
# 定义字符串变量
end5 = "s"
# 定义字符串变量
end6 = "e"
# 定义字符串变量
end7 = "B"
# 定义字符串变量
end8 = "u"
# 定义字符串变量
end9 = "r"
# 定义字符串变量
end10 = "g"
# 定义字符串变量
end11 = "e"
# 定义字符串变量
end12 = "r"

# watch that comma at the end. try removing it to see what happens
# 将字符串进行拼接并打印，打印语句结尾使用' '结尾，取代默认换行'\n'
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
# 将字符串进行拼接并打印
print(end7 + end8 + end9 + end10 + end11 + end12)

