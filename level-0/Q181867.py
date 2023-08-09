# x 사이의 개수 https://school.programmers.co.kr/learn/courses/30/lessons/181867

# 나의 풀이
def solution1(myString):
    x_idx = [idx for idx, s in enumerate(myString) if s == 'x']
    answer = list(map(lambda i: x_idx[i] - x_idx[i-1] - 1, range(1, len(x_idx))))

    answer.insert(0, x_idx[0])
    if x_idx[-1] < len(myString):
        answer.append(len((myString) - x_idx[-1] - 1))
    return answer


# 다른 사람의 풀이
def solution2(myString):
    return [len(s) for s in myString.split('x')]