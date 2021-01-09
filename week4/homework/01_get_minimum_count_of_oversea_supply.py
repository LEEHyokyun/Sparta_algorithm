import heapq

# heap을 쓰기위해 선언

# 공급날까지 회사가 재고가 있는지도 확인한다.
# 재고가 바닥나는 시점 이전까지 받을 수 있는
# 라면중 제일 많은 라면을 받는게 목표

# key1. 현재 재고의 상태에 따라 최고값을 받아야 한다.
# key2. 라면의 재고는 동적으로 변경된다.
# key3. 제일 많은 값만 가져가면 된다.
# key4. 데이터를 넣을 떄 마다 최대값을 동적으로 변경시키며
# key5. 최소, 최대값을 바로 꺼낼 수 있는 heap을 이용한다.

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):

    answer = 0
    current_day_index = 0
    max_heap = [] #현재 공급량이 떨어지지 않는 선에서 가져올수있는 최대 공급량

    # 일단 stock이 k보다는 많아야 함
    while stock < k:
        # date를 기준으로 반복
        for date_index in range(current_day_index, len(dates)):

            print(date_index, dates[date_index], stock, supplies[date_index])

            if dates[date_index] <= stock:
                heapq.heappush(max_heap, -supplies[date_index]) #지정된 heap 함수
            else:
                current_day_index = date_index
                break

        answer = answer + 1

        print("stock is", stock)

        stock = stock + -heapq.heappop(max_heap)

    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))