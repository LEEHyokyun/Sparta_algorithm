input = 20


def find_prime_list_under_number(number):
    prime_list = [] #input 변수는 정수이나 반환하는 값은 배열

    for n in range(2, number + 1): #for문 콜론 끝맺음, 변수받아서 일단 반복
        for i in prime_list: #소수만 이용하여 소수값을 찾을 수 있음
        #for i in range(2,n): #2부터 받은 변수의 -1까지 반복 (소수찾기위한 알고리즘)
            if n % i ==0:
                break #소수가 아니기 때문에 반복문 중단하고 다음 알고리즘으로
        else : #나누어 떨어지지 않으면(break가 한번도 발생하지 않았다면) 소수이기 떄문에 소수배열에 추가
            prime_list.append(n) #prime_list 배열에 추가

    return prime_list


result = find_prime_list_under_number(input)
print(result)