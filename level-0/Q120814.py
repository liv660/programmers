# 피자 나눠 먹기(1) https://school.programmers.co.kr/learn/courses/30/lessons/120814

# 나의 풀이
def solution1(n):
    return n//7 if n % 7 == 0 else n//7 + 1

# 다른 사람의 풀이
def solution2(n):
    return (n - 1) // 7 + 1