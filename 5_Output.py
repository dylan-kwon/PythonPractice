# coding=utf-8

my_name = 'Zed A. Shaw'
my_age = 35
my_height = 188
my_weight = 82
my_eyes = '파랑'
my_teeth = '하양'
my_hair = '갈색'

print "%s에 대해 이야기해 보죠." % my_name
print "키는 %d 센티미터고요." % my_height
print "몸무게는 %d 킬로그램이에요." % my_weight
print "눈은 %s이고 머리는 %s이에요." % (my_eyes, my_hair)
print "이는 보통 %s이고 커피를 먹으면 달라져요." % my_teeth

print "\n"

print "%d, %d, %d를 전부 더하면 %d랍니다." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

total = round(my_age + my_height + my_weight, 1)
print "%r, %r, %r를 전부 더하면 %r랍니다." % (my_age, my_height, my_weight, total)

