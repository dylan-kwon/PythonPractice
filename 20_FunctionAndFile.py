# coding=utf-8

from sys import argv

script, input_file = argv


def print_all(f):
    f.read()
    return


def rewind(f):
    f.seek(0)
    return


def print_a_line(line_count, f):

    print line_count, f.readline()
    return


current_file = open(input_file)

print "파일 전체를 출력해 봅시다."
print_all(current_file)

print "테이프처럼 되감아 봅시다."
rewind(current_file)

print "세 줄을 출력해 봅시다."

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
