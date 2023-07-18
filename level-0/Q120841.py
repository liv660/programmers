# 점의 위치 구하기 https://school.programmers.co.kr/learn/courses/30/lessons/120841

# 나의 풀이
def solution1(dot):
    if dot[0] > 0:
        return 1 if dot[1] > 0 else 4
    return 2 if dot[1] > 0 else 3

# 다른 사람의 풀이
def solution2(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0] > 0][dot[1] > 0]