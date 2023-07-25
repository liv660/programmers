# 접두사인지 확인하기 https://school.programmers.co.kr/learn/courses/30/lessons/181906

# 나의 풀이
def solution1(my_string, is_prefix):
    return int(is_prefix in my_string[:len(is_prefix)])

# 다른 사람의 풀이
def solution2(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))