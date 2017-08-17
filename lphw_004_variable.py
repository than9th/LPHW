# encoding: utf-8
"""
@ Author: Kunkai Su 
@ Contact: su.kk@qq.com
@ Site: www.geneureka.com
@ Project: LPHW
@ File: lphw_004_variable.py
@ Time: 2017/7/8 22:56:02

这一行开始写关于本文件的说明与解释
"""


cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
car_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passenger_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", car_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passenger_per_car, "in each car."
