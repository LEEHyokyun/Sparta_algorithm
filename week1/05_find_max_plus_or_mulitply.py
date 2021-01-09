# 곱하기, 더하기를 하여 가장 큰수가 나타나도록 하라
# 0이 나올떄는 더하기, 1이 나올때도 더하기가 더 효율적이다.

input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    multiply_sum = 0
    for number in array:
        if number <= 1 or multiply_sum <= 1:
            multiply_sum += number #변수, 여난되어 나온 총합도 모두 고려해야함
        else:
            multiply_sum *= number
    return multiply_sum


result = find_max_plus_or_multiply(input)
print(result)

#1차 반복문 - 시간복잡도는 N+C(상수)
#array 길이만큼 반복 - O(N)