# coding=utf-8

from sys import argv

script, file_name = argv

txt = open(file_name, 'r')

print "파일 %r의 내용" % file_name
print txt.read()
txt.close()

print "파일 이름을 다시 입력해주세요.",
file_again = raw_input('> ')

txt_again = open(file_again)
print txt_again.read()
txt_again.close()
