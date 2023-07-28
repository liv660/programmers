# 수 조작하기 1 https://school.programmers.co.kr/learn/courses/30/lessons/181926

# 나의 풀이
def solution1(n, control):
    w = control.count('w')
    a = control.count('a')
    s = control.count('s')
    d = control.count('d')

    answer = n + (w*1) - (s*1) + (d*10) - (a*10)
    return answer


# 다른 사람의 풀이
def solution2(n, control):
    key = dict(zip(['w', 's', 'a', 'd', [1, -1, 10, -10]]))
    return n + sum([key[c] for c in control])


# zip() - 요소를 묶어준다.
def hello_zip():
    numbers = [1, 2, 3]
    letters = ['A', 'B', 'C']
    for pair in zip(numbers, letters):
        print(pair)