# coding=utf-8


class Calculator(object):
    class_member = "ㅋㅋㅋ"

    def __init__(self):
        super(Calculator, self).__init__()
        self.value = 0

    def plus(self, plus):
        self.value += plus
        return self.value

    def minus(self, minus):
        self.value -= minus
        return self.value


c1 = Calculator()
c2 = Calculator()

print c1.plus(10)
print c1.minus(3)

print c2.plus(13)
print c2.plus(-3)

print Calculator.plus(c1, 1)
print Calculator.minus(c2, 1)

print "-" * 30


class CustomCalculator(Calculator):
    def __init__(self, name):
        super(CustomCalculator, self).__init__()
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def plus(self, plus):
        print super(CustomCalculator, self).plus(plus)

    def minus(self, minus):
        print super(CustomCalculator, self).minus(minus)


custom_c1 = CustomCalculator("cc1")
custom_c2 = CustomCalculator("cc2")

print custom_c1.get_name()
print custom_c2.get_name()

custom_c1.set_name("cc11")
custom_c2.set_name("cc22")

print custom_c1.get_name()
print custom_c2.get_name()

custom_c1.plus(5)
custom_c2.minus(3)

print "-" * 30

custom_c1.class_member = "@1"
print custom_c1.class_member
print custom_c2.class_member
Calculator.class_member = "@2"
print custom_c1.class_member
print custom_c2.class_member

print "-" * 30


