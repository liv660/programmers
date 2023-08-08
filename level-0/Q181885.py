# 할 일 목록 https://school.programmers.co.kr/learn/courses/30/lessons/181885

# 나의 풀이
def solution1(todo_list, finished):
    return list(map(lambda i: todo_list[i], filter(lambda v: not finished[v], range(len(todo_list)))))


# 다른 사람의 풀이 1
def solution2(todo_list, finished):
    return [work for idx, work in enumerate(todo_list) if not finished[idx]]



# 다른 사람의 풀이 2
def solution3(todo_list, finished):
    return [work for work, status in zip(todo_list, finished) if not status]