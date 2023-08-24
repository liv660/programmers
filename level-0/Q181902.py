# 문자 개수 세가 https://school.programmers.co.kr/learn/courses/30/lessons/181902

# 나의 풀이
def solution1(my_string):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    answer = dict(zip(alphabet, [0 for i in range(len(alphabet))]))
    for i in my_string:
       answer[str(i)] += 1
    return list(answer.values())


# 다른 사람의 풀이
def solution2(my_string):
    return [my_string.count(alphabet) for alphabet in 'abcdefghijklmnopqrstuvwxyz'.upper() + 'abcdefghijklmnopqrstuvwxyz']
