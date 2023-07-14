# 피자 나눠 먹기(3) https://school.programmers.co.kr/learn/courses/30/lessons/120816

# 나의 풀이
def solution1(slice, n):
    return n // slice if n % slice == 0 else n // slice + 1

# 다른 사람의 풀이
def solution2(slice, n):
    return ((n-1) // slice) + 1
