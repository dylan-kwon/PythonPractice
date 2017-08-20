# coding=utf-8

prompt = '> '

print "문이 두 개 있는 어두운 방에 들어왔스빈다. 1번과 2번중 어디로 갈래요?",
door = int(raw_input(prompt))

if door == 1:

    print """"
    치킨이 있다. 먹을까?
    1. 먹는다
    2. 지나친다
    """

    isEat = int(raw_input(prompt))
    if isEat == 1:
        print "식중독으로 사망"

    elif isEat == 2:
        print "굶주려서 사망"

    else:
        print "사망"

elif door == 2:
    print """
    돈이 떨어져 있다 먹을까?
    1. 줍는다
    2. 지나친다
    """

    isPickUp = int(raw_input(prompt))
    if isPickUp == 1:
        print "앞으로 잘 먹고 잘 산다"

    elif isPickUp == 2:
        print "굶주려서 사망"

    else:
        print "사망"

else:
    print "사망"
