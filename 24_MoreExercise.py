# coding=utf-8

print "모든 것을 연습해 봅시다."

print '\\를 이용해 \\n 새 줄이나 \\t 탭을 하는 탈출순서열에 대해 \'알아야만\' 합니다. '

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor compreshnd passion from intuition
and requires an explanation
\n\ttwhere there is non.
"""

print "---------------------"
print poem
print "---------------------"

five = 10 - 2 + 3 - 6
print "이 값은 다섯이여야 합니다: %d" % five

print "\n"

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "시작점: %d" % start_point
print "%d알, %d단지, %d상자가 있습니다." % (beans, jars, crates)

print "\n"

print "이렇게도 가능하다"
print "%d알, %d단지, %d상자가 있습니다." % (secret_formula(start_point))
