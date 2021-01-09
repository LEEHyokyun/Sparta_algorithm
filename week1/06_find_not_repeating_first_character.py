input = "abaabadac"


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26  # 가로 배열 #들여쓰기도 코딩에 영향을 미침

    for char in string: #전달받은 char 변수가
        if not char.isalpha():  #알파벳아니면 종료, 알파벳이면 계속 # 띄어쓰기 등 문자인지 아닌지 확인
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1  # index 값을 1씩 증가

    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord("a")))
            #빈도수 1인 알파벳을 위 변수에 저장해둔다

    for char in string:
        if char in not_repeating_character_array:
           return char  #현재 문자열 순서대로 맞게 바로 반환
    print(not_repeating_character_array)


result = find_not_repeating_character(input)
print(result)