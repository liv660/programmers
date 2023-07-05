# 짝수의 합 https://school.programmers.co.kr/learn/courses/30/lessons/120831

# 나의 풀이
def solution1(n):
    answer = 0

    n = n if n % 2 == 0 else n - 1
    while n > 0:
        answer += n
        n -= 2
    return answer

# 다른 사람의 풀이
def solution2(n):
    return sum([i for i in range(2, n + 1, 2)])