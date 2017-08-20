# coding=utf-8

people = 30
cars = 40
buses = 150

if cars > people:
    print "차가 많다"

elif cars < people:
    print "사람이 많다"

else:
    print "모르겠다"

if buses > cars:
    print "버스가 많다"

elif buses < cars:
    print "차가 많다"

else:
    print "모르겠다"

if not not (cars > people) & (people != buses):
    print "ㅋㅋㅋㅋ"
