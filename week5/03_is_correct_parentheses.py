# 균형잡힌 문자열을 배개변수로 받았을때 올바른 문자로열로 반환하기
# (, ) 개수가 같을때 올바른 배열로 바꿔서 반환하기
# deque을 이용해서 올바른 문자열인지 아닌지 확인하는 함수 만들기




from collections import deque

balanced_parentheses_string = "()))((()"

def is_correct_parenthesis(string): #올바른 괄호 문자열인지 확인할것 (by using deque)

    stack = []

    for s in string:
        if s == '(': #문자열 문자를 하나하나 비교하면서 열린괄호인지 비교
            stack.append(s) #열렸다면 스택에 추가
        elif stack: #stack이 존재하면서, input 문자열이 균형잡힌(열린괄호, 닫힌괄호 개수 동일) 문자열이라 가정
            stack.pop() #닫혀있다면 스택에서 제거
    return len(stack) == 0 #스택이 없다면 올바른 문자열이다.

#입력이 빈 문자열인경우, 빈 문자열을 반환

def reverse_parenthesis(string):
    # 문자열 u가 올바른 괄호 문자열이 아니라면
    # 빈 문자열에 첫번째 문자로 (을 붙이고, 문자열 v에 대해 재귀적으로 수행한 결과 문자열을 이어붙인다
    # )을 다시 붙인다. (그게 아래 알고리즘)
    # u의 첫번째 문자열과 마지막 문자를 제거하고, 나머지 문자열의 괄호방향을 뒤집어서 뒤에 붙인다
    reversed_string = ""
    for char in string:  # u 문자열은 첫번쨰 ~ 마지막 첫번째 문자 제거.
        if char == '(':
            reversed_string = reversed_string + ')'
        else:
            reversed_string = reversed_string + '('
    return reversed_string
   # "(" + change_to_correct_parenthesis(v) + ")" + reversed_string
   # 아래 change to correct 함수에서 호출된다.


def seperate_to_u_v(string):

    queue = deque(string)  # queue에 문자열을 deque에 담아서 저장하였다.
    left, right = 0, 0  # 개괄호, 폐괄호
    u, v = "", ""  # 각 빈 문자열로 초기화

    while queue:

        char = queue.popleft()
        u = u + char  # if문을 수행하면서 u 문자열에 추가한다.

        if char == '(':
            left = left + 1
        else:
            right = right + 1
        if left == right:
            break  # 개괄호와 폐괄호 개수가 같아지면 if문을 멈추고 아래로

    v = ''.join(list(queue))  # 큐에 남아있는 문자열은 v에 모두 넣어준다.
    # join뒤에 배열을 넣고, ''을 넣으면 그 기준으로 문자열을 합쳐준다.
    print(u, v)
    return u, v

    # 파이썬 콘솔에서 위 예시 확인가능.. 문자열들을 모두 붙여준다.
    # a = ["1", "2", "3"]
    # ''.join(a)
    # '123'

    # 문자열 w를, 두 균형잡힌 문자열인 u,v로 분리한다.
    # 단 u는 균형잡힌 괄호 문자열로 더이상 분리할수 없어야 하며
    # v는 빈 문자열이 될 수 있다.
    # ( 개수 = ) 개수, 이 조건부터 만족하는 문자열부터 꺼내보자.

def change_to_correct_parenthesis(string):
    if string == "": #문자열 없을 경우
        return ""
    u, v = seperate_to_u_v(string) # u,v 를 받았다.
    # 위 u,v 문자열을 받은후
    # 문자열 u가 올바른 괄호 문자열이라면
    # 문자열 v에 대해 균형잡힌 문자열 추출하는 과정부터 반복.
    # 각 단계별을 함수화한다.
    # 수행한 결과 문자열을 u에 이어붙인후에 반환 (그게 아래 알고리즘)
    if is_correct_parenthesis(u):
        return u + change_to_correct_parenthesis(v)

    else:
        return "(" + change_to_correct_parenthesis(v) + ")" + reverse_parenthesis(u[1:-1])

def get_correct_parentheses(balanced_parentheses_string):

    if is_correct_parenthesis(balanced_parentheses_string): #애초부터 올바른 문자열이라면
        return balanced_parentheses_string #바로 반환
    else:
        return change_to_correct_parenthesis(balanced_parentheses_string)


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!