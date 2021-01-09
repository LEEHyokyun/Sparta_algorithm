# 알파벳 26개 모두에 대한 빈도수를 저장하기위함

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26 # 가로 배열

    for char in string:

        if not char.isalpha():  # 띄어쓰기 등 문자인지 아닌지 확인
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1 #index 값을 1씩 증가

    return alphabet_occurrence_array
    # 이 부분을 채워보세요!

print(find_alphabet_occurrence_array("hello my name is sparta"))
print(ord("h"))
print(ord("a"))