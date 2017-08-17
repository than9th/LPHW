# encoding: utf-8
"""
@ Author: Kunkai Su 
@ Contact: su.kk@qq.com
@ Site: www.geneureka.com
@ Project: LPHW
@ File: lphw_005_more-variables-prints.py
@ Time: 2017/7/8 23:40:24

这一行开始写关于本文件的说明与解释
"""


my_name = '苏锟楷'
my_age = 34 # not a lie
my_height = 178 # cm
my_weight = 85 # kg
my_eyes= 'Black'
my_teeth = 'White'
my_hair = "Black"

print "Let's talk about %s." % my_name
print "He's %d cm tall." % my_height
print "He's %d kg heavy." % my_weight
print "Actually it's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "He's teeth are usually %s depending on the coffee." % my_teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d," % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
