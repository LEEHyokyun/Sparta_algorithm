#선택정렬은 첫번쨰 인덱스부터 정렬시작한다
#처음숫자 4는 이미 정렬되어있다고 기정한다

input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):  # 숫자 6부터시작, 배열크기
        print("i is", i)
        for j in range(i):
            print("j is", j)
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
                print(array)
            else:
                break # 반복문종료(정렬되어있는데 그 숫자보다도 크면 정렬할 이유가 없다)
                      # for문으로 올라감??
    return


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!