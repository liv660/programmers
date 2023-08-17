# 08.17

# 문자열 여러 번 뒤집기 https://school.programmers.co.kr/learn/courses/30/lessons/181913

# 나의 풀이
def solution1(my_string, queries):
    my_string = list(my_string)
    for s, e in queries:
        scope = len(list(range(s, e+1))) // 2

        idx = 0
        while idx < scope:
            temp = my_string[s+idx]
            my_string[s+idx] = my_string[e-idx]
            my_string[e-idx] = temp
            idx += 1
    return ''.join(my_string)


# 다른 사람의 풀이
def solution2(my_string, queries):
    for (s, e) in queries:
        my_string = my_string[:s] + my_string[s:e + 1][::-1] + my_string[e + 1:]
    return my_string