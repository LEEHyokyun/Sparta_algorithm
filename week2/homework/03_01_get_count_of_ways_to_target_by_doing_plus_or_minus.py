# 간소화해서 먼저 알고리즘 찾기
# 문제를 먼저 간소화한후에(모든 배열에 적용될 수 있는 알고리즘)
# 그 후 다른 배열을 적용하는 방식으로 해결
# +2 -3 +1 = 0
# -2 +3 -1 = 0

# 첫번쨰 가지는 ++ 다음에 + or -
# 두번째 가지는 +- 다음에 + or - ...
# 앞 부호를 고정시켜서 다음 부호를 + - 가지화 이런식으로 반복
# N-1 길이의 배열에서 마지막 원소를 + or - 한 가지수가 N 배열의 가지수가 됨.

numbers = [1,1,1,1,1]
target_number = 3

# 2 3 의 부호를 정해주고 마지막 1의 + or - 로 가지치기
result_count = 0

# all_ways = result = []
# 현재 들어있는 배열인 array
# 현재 인덱스 0 은 current_index
# 2, 3, 1
# 최초 실행시 array , 1, 0+2(아래건0-2), all_ways


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum):
    if current_index == len(numbers):
        if current_sum == target:
            global result_count #외부변수를 사용하기위한 키우드
            result_count = result_count + 1 #내부에서 외부변수를 쓰겠다
        return

    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1, current_sum + numbers[current_index])
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1, current_sum - numbers[current_index])




print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0))  # 5를 반환해야 합니다!
print(result_count) #0이 찍힌다?

# 문자열, 캐릭터는 파이썬 내부에서 파라미터로 넘기면 새로운 값을 생성.
# 함수에서 외부의 변수를 변경해주고힢다면 global이라는 키워드를 사용해야한다.
# 외부 변수이름을그대로 쓰고,