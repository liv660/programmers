# 정수 찾기 https://school.programmers.co.kr/learn/courses/30/lessons/181840

# 나의 풀이
def solution1(num_list, n):
    return 1 if num_list.count(n) > 0 else 0

# 다른 사람의 풀이
def solution2(num_list, n):
    return int(n in num_list)