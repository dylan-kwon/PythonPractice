# coding=utf-8

import abc


class A(object):
    class_member = 0

    def __init__(self):
        self.__instance_member = 1

    @property
    def instance_member(self):
        return self.__instance_member

    @instance_member.setter
    def instance_member(self, value):
        self.__instance_member = value

    @classmethod
    def class_method(cls):
        return cls.class_member

    @staticmethod
    def static_method():
        return A.class_member

    @abc.abstractmethod
    def abstract_method(self):
        raise BaseException

    def instance_method(self):
        return True


class B(A):
    class_member = 10

    def abstract_method(self):
        pass

    def instance_method(self):
        pass

a = A()
b = B()

'''''''''''''''''''''''''''''''''''''''''
            인스턴스 변수 체크
'''''''''''''''''''''''''''''''''''''''''
# print(a.instance_member)
# a.instance_member = 100
# print(a.instance_member)
#
# print(b.instance_member)

'''''''''''''''''''''''''''''''''''''''''
             클래스 변수 체크
'''''''''''''''''''''''''''''''''''''''''
# print(a.class_member)
# print(b.class_member)
#
# a.class_member = 10
# b.class_member = 20
#
# print(a.class_member)
# print(b.class_member)
#
# A.class_member = 30
#
# print(A.class_member)
# print(B.class_member)

'''''''''''''''''''''''''''''''''''''''''
              클래스 함수 체크
'''''''''''''''''''''''''''''''''''''''''
# print(A.class_method())
# print(B.class_method())
# A.class_member = 20
# print(A.class_method())
# print(B.class_method())

# print(a.class_method())
# print(b.class_method())
# A.class_member = 20
# print(a.class_method())
# print(b.class_method())

'''''''''''''''''''''''''''''''''''''''''
              스태틱 함수 체크
'''''''''''''''''''''''''''''''''''''''''
# print(A.static_method())
# print(B.static_method())
# A.class_member = 30
# print(A.static_method())
# print(B.static_method())

# print(a.static_method())
# print(b.static_method())
# a.class_member = 10
# print(b.static_method())
# print(b.static_method())
