# 코드 처리하기 https://school.programmers.co.kr/learn/courses/30/lessons/181932

# 나의 풀이
def solution1(code):
    mode = False
    answer = ''
    for i in range(len(code)):
        if code[i] != '1' and ((mode and i % 2 ==0) or (not mode and i % 2 == 0)):
            answer += code[i]
        if code[i] == '1':
            mode = not mode
    return answer if answer != '' else 'EMPTY'


# 다른 사람의 풀이
# 왜 mode를 고려 안해도 되는지 모르겠다
def solution2(code):
    return ''.join(code.split('1')[::2] or 'EMPTY')

