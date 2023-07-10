# 머쓱이보다 키 큰 사람 https://school.programmers.co.kr/learn/courses/30/lessons/120585

# 나의 풀이
def solution1(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
    return answer

# 다른 사람의 풀이
def solution2(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)
