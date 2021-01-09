input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    for num in array:  # num은 array 안의 숫자변수
        for compare_num in array:  # compare_num은 비교를 위한 숫자변수
            if compare_num in array:
                if num < compare_num:
                    break
        else:  # for문 break가 없으면 실행

            return num, compare_num

    # 이 부분을 채워보세요!


result = find_max_num(input)
print('maximum value, compare value = ', result)
