# coding=utf-8

print "몇 살이죠?",
age = int(raw_input())

print "키는 얼마죠?",
height = raw_input()

print "몸무게는 얼마죠?",
weight = raw_input()

print "네 나이는 %d살, 키는 %scm, 몸무게는 %skg이네요" % (
    age, height, weight)

print "뜬금없지만, 태양의 각지름은 %d 정도입니다.", """31'10""",
