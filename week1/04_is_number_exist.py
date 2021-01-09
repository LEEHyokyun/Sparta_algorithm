# 배열내 특정숫자가 존재한다면 true, 아니면 false 반환

input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for element in array:  #array 길이만큼 아래 연산이 실행
         if number == element: #비교연산 1번 실행
              return True #N*1 = N의 시간복잡도
                          #3이 첫번쨰 오면 바로, 나중에 오면 array 모두 봐야함
                          #즉, 최악일떄 N만큼의 성능, 최선일떄 1(바로 output)의 성능을 보임
                          #보통의 경우 최악의 성능으로 알고리즘의 성능을 따진다(빅오표기법).
    return False  #for문 반복후에 true가 없으면 false 반환


result = is_number_exist(3, input)
print(result)