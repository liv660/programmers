# 배열 만들기 1 https://school.programmers.co.kr/learn/courses/30/lessons/181901

# 나의 풀이
def solution1(n, k):
    return list(filter(lambda v: v % k == 0, range(1, 1+n)))

# 다른 사람의 풀이
def solution2(n, k):
    return [i for i in range(k, n+1, k)]