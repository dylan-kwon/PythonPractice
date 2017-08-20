# coding=utf-8

# stuff = {'name': 'zed', 'age': 36, "height": 6 * 12 + 2}
# print stuff
#
# print stuff["name"]
# print stuff['age']
# print stuff['height']
#
# stuff['city'] = "San Francisco"
# print stuff
#
# del stuff['city']
# print stuff

states = {
    "충청북도": "충북",
    "경상북도": "경북",
    "전라남도": "전남",
    "경기도": "경기",
    "강원도": "강원"
}

cities = {
    "전남": "광주",
    "강원": "원주",
    "경북": "대구",
}

print "\n"

cities["경기"] = "수원"
cities["충북"] = "충주"

print "-" * 30
print "경기도에는", cities["경기"]
print "충청북도에는", cities["충북"]

print "-" * 30
print "강원도의 약자는 %s" % states["강원도"]
print "경상북도의 약자는 %s" % states["경상북도"]

print "-" * 30
print "강원도에는 %s" % cities[states["강원도"]]
print "경상북도에는 %s" % cities[states["경상북도"]]

print "-" * 30
for state, abbrev in states.items():
    print "%s의 줄임말은 %s입니다." % (state, abbrev)

print "-" * 30
for abbrev, city in cities.items():
    print "%s에는 %s가 있습니다." % (abbrev, city)

print "-" * 30
for state, abbrev in states.items():
    print "%s의 줄임말은 %s이고, %s가 있습니다." \
          % (state, abbrev, cities[abbrev])

print "-" * 30
print "도 이름 약자를 안전하게 받아옵니다."
state = states.get("제주도", None)

if state is None:
    print "제주도는 없다"

else:
    print "제주도의 줄임말은 %s다" % state