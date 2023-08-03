# 더 크게 합치기 https://school.programmers.co.kr/learn/courses/30/lessons/181939

# 나의 풀이
def solution1(a, b):
    a, b = str(a), str(b)
    return a + b if (a + b) >= (b + a) else b + a


# 다른 사람의 풀이
def solution2(a, b):
    return int(max(f'{a}{b}', f'{b}{a}'))