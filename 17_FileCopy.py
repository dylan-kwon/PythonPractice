# coding=utf-8

from os.path import exists
from sys import argv

script, from_file, to_file = argv

print "%s에서 %s로 복사합니다." % (from_file, to_file)

in_file = open(from_file)
in_file_data = in_file.read()
print "in_file_data = %s" % in_file_data
print "입력 파일은 %d바이트 입니다." % len(in_file_data)

print "출력 파일이 존재하나요? %r" % exists(to_file)

print "준비되었습니다. 계속하려면 리턴 키를, 취소하려면 CTRL-C를 누르세요. ",
raw_input('> ')

out_file = open(to_file, 'w')
out_file.write(in_file_data)

print "모두 완료되었습니다."

in_file.close()
out_file.close()
