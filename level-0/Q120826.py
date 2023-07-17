# 특정 문자 제거하기 https://school.programmers.co.kr/learn/courses/30/lessons/120826

# 나의 풀이
def solution1(my_string, letter):
    answer = list(my_string)
    for i in range(my_string.count(letter)):
        answer.remove(letter)
    return ''.join(answer)

# 다른 사람의 풀이
def solution2(my_string, letter):
    return my_string.replace(letter, '')