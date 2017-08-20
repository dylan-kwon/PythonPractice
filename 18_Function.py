# coding=utf-8

def print_none():
    print "아무것도 받지 않음."


def print_one(arg1):
    print "실행인자1: %r" % arg1


def print_two(arg1, arg2):
    print "실행인자1: %r, 실행인자2: %r" % (arg1, arg2)


def print_two_again(*args):
    arg1, arg2 = args
    print "실행인자1: %r, 실행인자2: %r" % (arg1, arg2)


print_none()
print_one("First!!")
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
