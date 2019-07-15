'''
@message: 字符串和文本
            .format()

@Author: Raynor.shang
@since: 2019-07-15 16:48:43
@lastTime: 2019-07-15 17:25:36
@LastAuthor: Raynor.shang
'''

# 原文
"""
    types_of_people = 10
    x = f"There are {types_of_people} types of people."

    binary = "binary"
    do_not = "don't"
    y = f"Those who know {binary} and those who {do_not}."

    print(x)
    print(y)
    print(f"I said: {x}")
    print(f"I also said: '{y}'")

    hilarious = "False"
    joke_evaluation = "Isn't that joke so funny?! {}"

    print(joke_evaluation.format(hilarious))

    w = "This is the left side of ..."
    e = "a string with a right side."

    print(w + e)
"""

# 巩固练习：1.添加注释，解释作用
"""
    # 定义整型变量types_of_people，变量值为10
    types_of_people = 10
    # 定义字符串变量x，值为使用fstr格式化的字符串，注入types_of_people
    x = f"There are {types_of_people} types of people."

    # 定义字符串变量binary，值为"binary"
    binary = "binary"
    # 定义字符串变量do_not，值为"don't"
    do_not = "don't"
    # 使用fstr格式化字符串y，值为使用fstr格式化的字符串，注入binary、do_not
    y = f"Those who know {binary} and those who {do_not}."

    # 打印x
    print(x)
    # 打印y
    print(y)
    # 打印fstr格式化的字符串，注入x
    print(f"I said: {x}")
    # 打印fstr格式化的字符串，注入y
    print(f"I also said: '{y}'")

    # 定义字符串变量hilarious，值为"False"
    hilarious = "False"
    # 定义字符串变量joke_evaluation，值为"Isn't that joke so funny?! {}"
    joke_evaluation = "Isn't that joke so funny?! {}"

    # 打印.format()格式化的字符串变量，注入hilarious
    print(joke_evaluation.format(hilarious))

    # 定义字符串变量w，值为"This is the left side of ..."
    w = "This is the left side of ..."
    # 定义字符串变量e，值为"a string with a right side."
    e = "a string with a right side."

    # w变量与e变量进行拼接后打印输入
    print(w + e)
"""

# 巩固练习：2.找出“把一个字符串放进另一个字符串”的位置，共计4处，以 ○ 标识
"""
# 定义整型变量types_of_people，变量值为10
    types_of_people = 10
    # 定义字符串变量x，值为使用fstr格式化的字符串，注入types_of_people              
    x = f"There are {types_of_people} types of people."

    # 定义字符串变量binary，值为"binary"
    binary = "binary"
    # 定义字符串变量do_not，值为"don't"
    do_not = "don't"
    # 使用fstr格式化字符串y，值为使用fstr格式化的字符串，注入binary、do_not         
    y = f"Those who know {binary} and those who {do_not}."                      # ○

    # 打印x
    print(x)
    # 打印y
    print(y)
    # 打印fstr格式化的字符串，注入x
    print(f"I said: {x}")                                                       # ○ 
    # 打印fstr格式化的字符串，注入y
    print(f"I also said: '{y}'")                                                # ○

    # 定义字符串变量hilarious，值为"False"
    hilarious = "False"
    # 定义字符串变量joke_evaluation，值为"Isn't that joke so funny?! {}"
    joke_evaluation = "Isn't that joke so funny?! {}"

    # 打印.format()格式化的字符串变量，注入hilarious
    print(joke_evaluation.format(hilarious))                                    # ○

    # 定义字符串变量w，值为"This is the left side of ..."
    w = "This is the left side of ..."
    # 定义字符串变量e，值为"a string with a right side."
    e = "a string with a right side."

    # w变量与e变量进行拼接后打印输入
    print(w + e)
"""

""" 
    # 巩固练习：3.2中确定是否只有四处
    # 确定，前3处为f-string格式化方式，最后一处为.format()格式化方式
    # 第112行理论上是产生了一个新的字符串，并且其值与w与e拼接后的值相同，但是并不是把w或e放入其中
"""
# 巩固练习：4.解释为什么w和e用+进行连接便可生成一个更长的字符串
# 本质上进行了字符串的拼接，当+运算符左右两侧均为字符串变量时将会把两侧变量进行拼接，并产生一个新的，值与两个字符串拼接后一致的新字符串。