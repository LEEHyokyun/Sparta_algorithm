array = [5, 3, 2, 1, 6, 8, 7, 4]

# 5 3 > 3 5
# 2 1 > 1 2
# 6 8 > 6 8
# 7 4 > 4 7

# 35 12 > 1235
# 68 47 > 4678

# 1235 4678 > 12345678

# 각 단계뼐 O(N)만큼의 시간복잡도
# k단계시 (N/2)^k .. log2N 의 시간복잡도.
# log2N * O(N) = o(NlogN)

def merge_sort(array):

    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_array = merge_sort(array[:mid]) #0부터 mid인덱스까지의 array
    right_array = merge_sort(array[mid:len(array)]) #mid부터 인덱스까지의 array

    print(array)
    print('left_array', left_array)
    print('right_array', right_array)

    return merge(left_array, right_array)

def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    return result


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!