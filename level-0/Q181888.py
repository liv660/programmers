# n개 간격의 원소들 https://school.programmers.co.kr/learn/courses/30/lessons/181888

# 나의 풀이
def solution1(num_list, n):
    return [num_list[i] for i in list(range(0, len(num_list), n))]

# 다른 사람의 풀이
def solution2(num_list, n):
    return num_list[::2]