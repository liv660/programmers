# 중복된 숫자 개수 https://school.programmers.co.kr/learn/courses/30/lessons/120583

# 나의 풀이
def solution1(array, n):
    return len(list(filter(lambda v: n == v, array)))

# 다른 사람의 풀이
def solution2(array, n):
    return array.count(n)