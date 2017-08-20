# coding=utf-8

def break_word(stuff):
    # 이 함수는 문자열을 단어로 쪼개 줍니다.
    words = stuff.split(' ')
    return words


def sort_words(words):
    # 단어를 정렬합니다.
    return sorted(words)


def print_first_word(words):
    # 첫 단어를 꺼내서 출력합니다.
    return words.pop(0)


def print_last_word(words):
    # 마지막 단어를 꺼내서 출력합니다.
    return words.pop()


def sort_sentence(sentence):
    # 한 문장을 통째로 받아 단어를 정렬해서 반환합니다.
    words = break_word(sentence)
    return sorted(words)


def print_first_and_last(sentence):
    # 문장의 처음과 마지막 단어를 출력합니다.
    words = break_word(sentence)
    return print_first_word(words), print_last_word(words)


def print_first_and_last_sorted(sentence):
    # 단어를 정렬하고 처음과 마지막 단어를 출력합니다.
    words = sort_sentence(sentence)
    return print_first_word(words), print_last_word(words)


sentence = "All good things come to those who wait."

words = break_word(sentence)
sorted_words = sort_words(words)

print print_first_word(words)
print print_last_word(words)

print print_first_word(sorted_words)
print print_last_word(sorted_words)

print "%s, %s" % print_first_and_last(sentence)
print "%s, %s" % print_first_and_last_sorted(sentence)