# n의 배수 https://school.programmers.co.kr/learn/courses/30/lessons/181937

# 나의 풀이
def solution1(num, n):
    return 1 if num % n == 0 else 0

# 다른 사람의 풀이
def solution2(num, n):
    return int(not(num % n))