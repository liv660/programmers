# 조건에 맞게 수열 변환하기 3 https://school.programmers.co.kr/learn/courses/30/lessons/181835

# 나의 풀이
def solution1(arr, k):
    if k % 2 != 0: # k가 홀수
        for i in range(0, len(arr)):
            arr[i] *= k
    else:
        for i in range(0, len(arr)):
            arr[i] += k
    return arr

# 다른 사람의 풀이
def solution2(arr, k):
    return [(i * k) if k % 2 != 0 else (i + k) for i in arr]