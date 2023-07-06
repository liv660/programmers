# 배열 원소의 길이 https://school.programmers.co.kr/learn/courses/30/lessons/120854

# 나의 풀이
def solution1(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer

# 다른 사람의 풀이
def solution2(strlist):
    return list(map(len, strlist))
