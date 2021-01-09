# 비싼거 순서대로 비싼 할인율을 적용받으면 된다
# 일단 비싼거 순서대로 정렬

shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

def get_max_discounted_price(prices, coupons):

    prices.sort(reverse=True) #오름차순으로 정리
    coupons.sort(reverse=True) #오름차순 정리

    price_index = 0
    coupon_index = 0
    max_discounted_price = 0

    while price_index < len(prices) and coupon_index < len(coupons):

        max_discounted_price = max_discounted_price + prices[price_index] * (100 - coupons[coupon_index]) / 100
        price_index = price_index + 1
        coupon_index = coupon_index + 1

    while price_index < len(prices):
        max_discounted_price = max_discounted_price + prices[price_index]
        price_index = price_index + 1

    return max_discounted_price


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.