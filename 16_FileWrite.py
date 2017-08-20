# coding=utf-8

from sys import argv

script, file_name = argv

print "파일 여는 중..."
file = open(file_name, 'w')

print "%r 파일 내용을 지웁니다. 안녕히!" % file_name
file.truncate()

print "이제 세 줄에 들어갈 내용을 묻겠습니다."

line1 = raw_input("1줄: ")
line2 = raw_input("2줄: ")
line3 = raw_input("3줄: ")

print "위 내용을 파일에 씁니다."

# file.write(line1)
# file.write('\n')
# file.write(line2)
# file.write('\n')
# file.write(line3)
# file.write('\n')
newLine = "%r\n%r\n%r" % (line1, line2, line3)
file.write(newLine)

print "작성 완료.. 파일을 닫습니다."

file.close()
