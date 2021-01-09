#알파벳을 모두 대입하여 알파벳이 몇번 나오는지 세기

input = "hello my name is sparta"


def find_max_occurred_alphabet(string): # 함수 끝맺음
    alphabet_occurrence_array = [0] * 26  # 가로 배열 #들여쓰기도 코딩에 영향을 미침

    for char in string:
        if not char.isalpha(): #띄어쓰기 등 문자인지 아닌지 확인
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1 #index 값을 1씩 증가

    max_occurrence = 0
    max_alphabet_index = 0

    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurrence
    print(max_alphabet_index)

    return chr(max_alphabet_index + ord("a"))
    #아스키코드를 다시 문자로 바꾸기(숫자를 문자로해서 알파벳변환)
    #
    # 이 부분을 채워보세요!


result = find_max_occurred_alphabet(input)
print(result)