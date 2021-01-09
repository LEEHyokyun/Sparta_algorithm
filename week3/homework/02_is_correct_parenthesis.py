# 1. 순차탐색
# ( 괄호 열림
# ( ( 괄호 또 열림
# ) 괄호 닫힘, 아까 열린 것 중에 바깥 열린 것이 먼저 완료됨
# ) 괄호 닫힘, 안쪽 열린 것이 닫힘
# 괄호 열림 > 괄호 닫힘, 완료

# 2. 두번째
# ( 괄호 열림
# ( 괄호 열림
# ((( 괄호 또 열림
# ) 괄호 닫힘 > 현재 열린 괄호는 2개
# 열림 괄호가 남아있으므로 괄호쌍은 False

# 1. 닫는 괄호가 나오면 바로 직전에 열린 괄호가 있는지 탐색한다
# 2. 열린 괄호는 계속 저장해야한다.
# Stack에 열린 괄호를 쌓고 --- ["(", "("]
# 닫는 괄호가 나오면 열린 괄호를 하나 제거
# 또 닫는 괄호가 나오면 열린 괄호를 하나 또 제거!
# 스택이 비어있지 않다면 False

s = "(())()"


def is_correct_parenthesis(string):

    stack = []

    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i) # 어떤 값이 들어가도 상관 없음, 여부가 중요
        elif string[i] == ")": # 닫는 괄호가 나오면 #elif : 그렇지 않다면
            if len(stack) == 0: #여는 괄호가 없을때 나와도 실패
                return False
            else:
                stack.pop()

    if len(stack) != 0 :
        return False

    else:
        return True

    return


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!