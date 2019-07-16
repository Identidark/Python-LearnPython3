'''
@message: 变量和命名练习，为什么报错
            出错原因：作者使用的变量名存在错误，并未被定义。

@Author: Raynor.shang
@since: 2019-07-15 15:21:53
@lastTime: 2019-07-15 16:07:55
@LastAuthor: Raynor.shang
'''

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")