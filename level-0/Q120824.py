# 짝수 홀수 개수 https://school.programmers.co.kr/learn/courses/30/lessons/120824

# 냐의 풀이
def solution1(num_list):
    even = 0
    odd = 0

    for i in num_list:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return [even, odd]

# 다른 사람의 풀이
def solution2(num_list):
    answer = [0, 0]
    for i in num_list:
        answer[i % 2] += 1
    return answer