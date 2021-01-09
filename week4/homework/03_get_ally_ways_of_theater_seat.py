# 1 2 3 4 5 6 7 8 9 있을때
# 4 7 좌석이 고정되어있을때
# 1 2 3 / 5 6 / 8 9 어떻게 옮길 수 있을까.

# ex)

# 1 2 3 (3)
# 1 2 3 / 2 1 3 / 1 3 2

# 1 2 3 4 (5)
# 1 2 3 4 / 1 2 4 3 / 1 3 2 4 / 2 1 3 4 / 2 1 4 3

# 1 2 3 4 5 (8)
# 1 2 3 4 5 / 1 2 3 5 4 / 2 1 3 4 5 / 2 1 3 5 4 / 1 2 4 3 5 / 2 1 4 3 5
# 2 1 3 4 5 / 1 3 2 4 5

# 피보나치수열을 이용한다.

# 총 좌석의 자리가 i개 있다고 하고, i가 i에 앉았다면
# 이 경우 앞의 i - 1 좌석들을 맘껏 배치할 수 있는 경우의 수가 됨


# 총 좌석의 자리가 i개 있다고 하고, i가 i-1에 앉는다면
# i-1가 i-2에 앉을 경우, i번째가 공석이 돼서 앉을 방법이 없게 되고
# 따라서 i-1은 i번째에 무조건 앉아야 가능한 경우가 나온다.
# 이 경우 i - 2 좌석들을 맘껏 배치할 수 있는 경우의 수가 됨

# F(N) = N 명의 사람들을 좌석에 배치하는 방법은
#      = F(N-1) + F(N-2)

# 문제에서
# 1 2 3 경우는 F(3)
# 5 6은 F(2)
# 8 9은 F(2)

seat_count = 9
vip_seat_array = [4, 7]

memo = {
    1: 1,
    2: 2
}


# 1. 만약 메모에 있으면 그 값을 바로 반환하고
# 2. 없으면 아까 수식대로 구한다.
# 3. 그리고 그 값을 다시 메모에 기록한다.

def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:  # n이 이미 구한 값인지
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo  # memo에 저장하고 반환한다.

    return nth_fibo



def get_all_ways_of_theater_seat(total_count, fixed_seat_array):

    all_ways = 1 # 가지수를 저장할 변수
    current_index = 0

    for fixed_seat in fixed_seat_array: #배열안을 순환하는 또 다른 변수
        fixed_seat_index = fixed_seat - 1 #인덱스가 아니라 번호, 번호화


        count_of_ways = fibo_dynamic_programming(fixed_seat_index - current_index, memo)  #고정된 좌석을가지고, 각 사이마다 나올수있는 경우의 수
        all_ways = all_ways * count_of_ways
        current_index = fixed_seat_index + 1

    count_of_ways = fibo_dynamic_programming(total_count - current_index, memo) # 고정된 좌석 사이 모두 구하고, 그 뒤 항목에 대한 경우의 수
    all_ways = all_ways * count_of_ways
    return all_ways


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))