'''
@message: 更多的变量和打印

@Author: Raynor.shang
@since: 2019-07-15 16:17:28
@lastTime: 2019-07-15 16:43:11
@LastAuthor: Raynor.shang
'''

# 原文
""" 
    my_name = "Zed A. Shaw"
    my_age = 35 # not a lie
    my_height = 74 # inches
    my_weight = 180 # lbs same as me lol
    my_eyes = 'Blue'
    my_teeth = 'White'
    my_hair = 'Brown'

    print(f"Let's talk about {my_name}.")
    print(f"He's {my_height} inches tall.")
    print(f"He's {my_weight} pounds heavy.")
    print("Actually that's not too heavy.")
    print(f"He's got {my_eyes} eyes and {my_hair} hair.")
    print(f"His teeth are usually {my_teeth} depending on the coffee.")

    # this line is tricky, try to get it exactly right
    total = my_age + my_height + my_weight
    print(f"If I add {my_age}， {my_height}, and {my_weight} I get {total}.")
"""
# 巩固练习：1.去除变量名的"_my"部分
""" 
    name = "Zed A. Shaw"
    age = 35 # not a lie
    height = 74 # inches
    weight = 180 # lbs same as me lol
    eyes = 'Blue'
    teeth = 'White'
    hair = 'Brown'

    print(f"Let's talk about {name}.")
    print(f"He's {height} inches tall.")
    print(f"He's {weight} pounds heavy.")
    print("Actually that's not too heavy.")
    print(f"He's got {eyes} eyes and {hair} hair.")
    print(f"His teeth are usually {teeth} depending on the coffee.")

    # this line is tricky, try to get it exactly right
    total = age + height + weight
    print(f"If I add {age}, {height}, and {weight} I get {total}.")
"""

# 巩固练习：转换英寸与磅为厘米与千克，使用公式
name = "Zed A. Shaw"
age = 35                 # not a lie
height = round(74 / 0.39370)    # inches
weight = round(180 / 2.2046)    # lbs same as me lol
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
