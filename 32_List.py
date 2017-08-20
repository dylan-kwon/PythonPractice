# # coding=utf-8

int_list = [4, 1, 2, 3, 5]
str_list = ['b', 'c', 'e', 'a', 'd']
mix_list = ['c', 1, 'a', 3, 'b', 2]
dimensional_list = [3, 4, 1, ['c', 'a', 'b'], 2]

print "\nDefault List"

print int_list
print str_list
print mix_list
print dimensional_list

# print "\nSort List"

# int_list.sort()
# print int_list

# str_list.sort()
# print str_list
#
# mix_list.sort()
# print mix_list

# dimensional_list.sort()
# dimensional_list[4].sort()
# print dimensional_list

print "\nSliceing List"

print int_list[0:3]
print str_list[3:]
print mix_list[:2]
print dimensional_list[3][0:2]

print "\nlist + list"

print int_list + str_list

print "\nlist * int"

print mix_list * 5

print "\nChange Value"

int_list[2] = 999
print int_list

str_list[2] = ['x', 'y', 'z']
print str_list

mix_list[:2] = [999, 'y', 'z']
print mix_list

print "\nDelete List"

dimensional_list[1:4] = []
print dimensional_list

del int_list[0:3]
print int_list

mix_list.remove(3)
print mix_list

print "\nAppand List"

int_list.append(6)
print int_list

str_list.append('f')
print str_list

mix_list.append("!!")
print mix_list

dimensional_list.append([1, 2, '3'])
print dimensional_list

print "\nIndex List"

print int_list.index(6)

print "\nInsert List"

int_list.insert(0, 999)
int_list.insert(3, 555)
print int_list

print "\nCount List"

print dimensional_list.count(3)

print "\nExtend List"

int_list.extend([5, 5, 5])
print int_list

int_list[0:0] = [6, 6, 6]
print int_list

print "\n"

# 리스트 객체 생성
listtt = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# value를 제일 뒤에 추가
listtt.append('value')

# 제일 뒤의 값을 꺼냄
listtt.pop()

# 인덱스 0번의 값을 꺼냄
listtt.pop(0)

# value가 몇 번째 인덱스에 있는지 찾음
print listtt.index(5)

# 처음으로 나오는 값(3)을 삭제
listtt.remove(3)

# 2번 인덱스에 value를 추가
listtt.insert(2, 'value')

# 해당 값을 추가
listtt.extend([444, 555, 666])

# extend와의 차이점 확인
listtt.append([777, 888, 999])

# 해당 값(2)의 개수를 구함
print listtt.count(2)

del listtt[0:2]

print listtt
