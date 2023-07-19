# 배열의 유사도 https://school.programmers.co.kr/learn/courses/30/lessons/120903

# 나의 풀이
def solution1(s1, s2):
    answer = 0
    for i in s1:
        if i in s2:
            answer += 1
    return answer

# 다른 사람의 풀이
def solution2(s1, s2):
    return len(set(s1)&set(s2))