# l로 만들기 https://school.programmers.co.kr/learn/courses/30/lessons/181834

# 나의 풀이
def solution1(myString):
    return ''.join(['l' if ord(i) < 108 else i for i in myString])


# 다른 사람의 풀이
# translate(str.maketrans('abc', '111'))
# 지정한 문자(abc)를 특정 문자(111)로 변환시킬 수 있다.
def solution2(myString):
    return myString.translate(str.maketrans('abcdefghijk', 'lllllllllll'))

