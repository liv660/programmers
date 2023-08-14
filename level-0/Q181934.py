# 조건 문자열 https://school.programmers.co.kr/learn/courses/30/lessons/181934

# 나의 풀이
def solution1(ineq, eq, n, m):
    if eq == '=':
        return int(n >= m) if ineq == '>' else int(n <= m)
    return int(n > m) if ineq == '>' else int(n < m)


# 다른 사람의 풀이
def solution2(ineq, eq, n, m):
    return int(eval(str(n) + ineq + eq.replace('!', '') + str(m)))