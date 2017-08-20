# coding=utf-8

def start_while(count):
    numbers = []
    i = 0
    while i < count:
        print "꼭대기에서 i는 %d" % i
        numbers.append(i)

        i += 1
        print "숫자는 이제 %r" % numbers
        print "바닥에서 i는 %d" % i

    # for i in range(0, count):
    #     print "꼭대기에서 i는 %d" % i
    #     numbers.append(i)
    #
    #     print "숫자는 이제 %r" % numbers
    #     print "바닥에서 i는 %d" % i

    return numbers

count = int(raw_input("반복 횟수 > "))
print "\nWhile 결과: %s" % start_while(count)
