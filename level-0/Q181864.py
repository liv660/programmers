# 문자열 바꿔서 찾기 https://school.programmers.co.kr/learn/courses/30/lessons/181864

# 나의 풀이
def solution1(myString, pat):
    my_string = ''
    for i in myString:
        my_string += 'B' if i == 'A' else 'A'
    return int(pat in my_string)


# 다른 사람의 풀이
def solution2(myString, pat):
    return int(pat in myString.replace('A', 'C').replace('B', 'A').replace('C', 'B'))