# coding=utf-8

# file = "17_FileCopy1.txt"
#
# with open(file) as f:
#     print f.read()
#
# assert 10 > 12, "21"
#
# try:
#     raise ValueError("valueError")
#
# except ValueError, e:
#     print e, "12"
#
# except ImportError, e:
#     print e
#
# finally:
#     print "finally"

def gen():
    val = 111111
    while True:
        val = (yield val) * 111111


g = gen()
print next(g)
print g.send(2)
print g.send(4)
