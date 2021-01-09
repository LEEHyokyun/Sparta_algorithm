input = [3, 5, 6, 1, 2, 4]
max_num = 3  # 지정변수


def find_max_num(array):
    max_num = array[0]  # array, 입력된 배열의 0번째 문자, 원소를 변수로 일단 지정.
    for num in array:
        if num > max_num:
            max_num = num

    return max_num

    # 이 부분을 채워보세요!
result = find_max_num(input)
# 함수값에 대한 결과변수를 지정해줘야함
# input은 배열변수이므로 함수매개변수도 array로

print(result)
