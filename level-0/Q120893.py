# 대문자와 소문자 https://school.programmers.co.kr/learn/courses/30/lessons/120893

# 나의 풀이
def solution1(my_string):
    return ''.join([i.lower() if ord(i) < 97 else i.upper() for i in list(my_string)])


# 다른 사람의 풀이
# swapcase(), 영문 대소문자가 상호 변환된 문자열을 반환한다.
def solution2(my_string):
    return my_string.swapcase()