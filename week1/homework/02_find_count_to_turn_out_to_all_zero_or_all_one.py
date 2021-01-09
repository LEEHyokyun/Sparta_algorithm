input = "011110"
# 0에서 1로 문자열이 전환되는 순간, count_to_all_zero 1증가
# 1에서 0으로 문자열이 전환되는 순간, count_to_all_one 1증가

# 1) 뒤집어질때, 2) 첫번째 원소가 0인지 1인지에 따라 숫자를 추가해줘야함

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0
    if string[0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1

    for i in range(len(string) - 1): #입력된 문자열에서 1제외한 만큼 반복
        if string[i] != string[i+1]: #i번째와 i+1번째 원소가 다르다면
            if string[i+1] == '0':
                count_to_all_one += 1
            if string[i+1]=='1':
                count_to_all_zero += 1
    print (count_to_all_one, count_to_all_zero)


    return min(count_to_all_zero, count_to_all_one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)