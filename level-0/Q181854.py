# 배열의 길이에 따라 다른 연산하기 https://school.programmers.co.kr/learn/courses/30/lessons/181854

# 나의 풀이
def solution1(arr, n):
    arr_temp = list(dict(enumerate(arr)).items())
    idx_range = arr_temp[::2] if len(arr) % 2 else arr_temp[1::2]

    for i in idx_range:
        arr[i[0]] = i[1] + n
    return arr


# 다른 사람의 풀이
def solution2(arr, n):
    arr_len = len(arr)

    if arr_len % 2:
        for i in range(0, arr_len, 2):
            arr[i] += n
    else:
        for i in range(1, arr_len, 2):
            arr[i] += n
    return arr


# 다른 사람의 풀이를 참고하여 나의 풀이 수정
def solution3(arr, n):
    start = 0 if len(arr) % 2 else 1

    for i in range(start, len(arr), 2):
        arr[i] += n
    return arr
