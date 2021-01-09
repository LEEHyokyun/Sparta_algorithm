# 회문인지 아닌지 검사하는 알고리즘

input = "abcba"


def is_palindrome(string):
    n = len(string) #문자열의 길이
    for i in range(n): #회문조회, i부터 n-1까지 반복
        if string[i] != string[n-1-i]: # 맨뒤에 있는 문자열은 n-1임.
            return False              # 1 더 뺴줘야함


    return True


print(is_palindrome(input))