'''
@message: 打印，打印
            
@Author: Raynor.shang
@since: 2019-07-16 08:31:04
@lastTime: 2019-07-16 08:40:33
@LastAuthor: Raynor.shang
'''

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))