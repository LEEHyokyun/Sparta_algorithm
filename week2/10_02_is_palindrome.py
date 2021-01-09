# 회문인지 아닌지 검사하는 알고리즘
# 소주만병만주소 > 주만병만주 > 만병만 > 병
# 문자열을 줄여나가는 방식으로 재귀함수이용

input = "abcba"


def is_palindrome(string):
    if string[0] != string[-1]:
        return False #다르면 False 출력
    if len(string) <= 1:
        return True
    return is_palindrome(string[1:-1])

# abcba
# 1,2 조건 통과하고 3 조건으로, 문자열이 처음 끝 빼고 반환됨
# 또 그 문자열이 반복..

print(is_palindrome(input))