# 순서쌍의 개수 https://school.programmers.co.kr/learn/courses/30/lessons/120836

# 나의 풀이
def solution1(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += 1
    return answer

# 다른 사람의 풀이
# filter(조건 함수, 순회 가능한 데이터)
# range만큼 lambda식을 실행한 결과 list의 길이를 반환한다.
def solution2(n):
    return len(list(filter(lambda v: n % (v+1) == 0, range(n))))