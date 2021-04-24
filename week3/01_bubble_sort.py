#배열의 크기 -1만큼 반복한다.

input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    n = len(array)
    print("n is", n)
    for i in range(n - 1):
        print("i is", i)
        for j in range(n - i - 1):  # i만큼 반복하면서 이미 정렬, i 제외
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j] #순서 바꾸는 명령어
            print("J is", j)
    return


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!