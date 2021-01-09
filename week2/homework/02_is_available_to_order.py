# 이거 False 출력된다....
# 정렬할 필요없이 쉽게 조회하는 방법
# 집합자료?
# set 함수 사용하여
# a = set([1,2,3,4,1,]) 입력시
# a 라는 배열은 중복을 허용하지 않는 자료형으로 1 2 3 4 만 남긴다.

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus_set = set(menus) #집합자료 함수로 중복되는거 제외
    for order in orders:
        if order not in menus_set:
            return False

    return True

def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array)-1 #array 배열 index 마지막 값
    current_guess = (current_max + current_min) // 2

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1 #범위를 위로
        else:
            current_max = current_guess -1 #범위를 아래로
        current_guess = (current_max + current_min) // 2

    return False

result = is_available_to_order(shop_menus, shop_orders)
print(result)