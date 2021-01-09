#이진탐색의 기본은 그 중간부터 시작하는것

finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

#    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# 1단계 : 최소값 - 최대값을 더해서 그 절반인 8(시도값으로 정의)부터 시작한다.
# 2단계 : 9부터 16으로 되고, 시도값은 12임
# 3단계 : 13부터 16으로 되고, 시도값은 14임, 함수 끝

def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array)-1 #array 배열 index 마지막 값
    current_guess = (current_max + current_min) // 2

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1 #범위를 위로
        else:
            current_max = current_guess -1 #범위를 아래로

        current_guess = (current_max + current_min) // 2

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)