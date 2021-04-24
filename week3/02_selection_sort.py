#n번째 최소값 정렬이 완료되면 n+1번째 숫자부터 비교시작

input = [4, 6, 2, 9, 1]

def selection_sort(array):
    n = len(array)

    for i in range(n - 1):  # 비교는 정렬크기의 -1
        min_index = i
        for j in range(n - i):
            if array[i+j] < array[min_index]: #i+j가 현재 인덱스임
                min_index = i + j
        array[i], array[min_index] = array[min_index], array[i]

        print(array)

selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!