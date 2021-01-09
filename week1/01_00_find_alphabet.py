print("a".isalpha())
# 지정변수가 문자인지 확인

array = "Hello world"
# 문자열의 해당 자리의 문자가 문자인지 확인
print(array[2].isalpha())
print(array[5].isalpha())

alphabet_occurence_array = [0]*26
# 해당 배열에는 원소 0이 26개로 배열되어 저장됨

ord("a")
print(ord('a')) #97, 아스키코드
print(ord('a')-ord('c'))