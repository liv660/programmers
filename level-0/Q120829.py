# 각도기 https://school.programmers.co.kr/learn/courses/30/lessons/120829

# 나의 풀이
def solution1(angle):
    if angle < 90:
        return 1
    if angle == 90:
        return 2
    if angle < 180:
        return 3
    return 4


# 다른 사람의 풀이
def solution2(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer
