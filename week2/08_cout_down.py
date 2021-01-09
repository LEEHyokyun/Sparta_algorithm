def count_down(number):
    if number < 0:
        return
    print(number)  # number를 출력하고
    count_down(number-1) # 자기 자신 함수를 부르는 재귀구조
                           # count_down 함수를 number - 1 인자를 주고 다시 호출한다!


count_down(60)

# 60부터 시작해서 0까지는 되었으나 끝도없이 반복..
# 재귀함수 호출시는 반드시 종료시점을 알려줘야함! (무한반복방지!)