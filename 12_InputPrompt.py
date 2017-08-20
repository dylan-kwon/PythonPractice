# coding=utf-8

age = int(raw_input("몇 살이죠? "))
height = raw_input("키는 얼마죠? ")
weight = raw_input("몸무게는 얼마죠? ")

print """네 나이는 %d살, 키는 %scm, 몸무게는 %skg이네요""" % (
    age, height, weight)

