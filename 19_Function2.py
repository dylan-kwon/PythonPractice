# coding=utf-8

def cheese_and_crackers(cheese_count, boxes_of_creackers):
    print "치즈가 %d개 있어요!" % cheese_count
    print "크래커가 %d상자 있어요!" % boxes_of_creackers
    print "파티 벌이기에 충분하네요"
    print "담요 한 장 가져오세요\n"


print "함수에 그냥 숫자를 직접 줄 수 있습니다."
cheese_and_crackers(20, 30)

print "스크립트의 변수를 쓸 수도 있고요."
amount_of_cheese = 10
amoun_of_creakers = 50
cheese_and_crackers(amoun_of_creakers, amoun_of_creakers)

print "안에서 계산도 가능하다."
cheese_and_crackers(10 + 20, amoun_of_creakers - 20)

print "입력도 가능하다."
cheese_and_crackers(
    int(raw_input("cheese = ")),
    int(raw_input("creackers = "))
)
