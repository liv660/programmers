# 옷가게 할인 받기 https://school.programmers.co.kr/learn/courses/30/lessons/120818

# 나의 풀이
def solution1(price):
    if price >= 500000:
        return int(price - price*0.2)
    if price >= 300000:
        return int(price - price*0.1)
    if price >= 100000:
        return int(price - price * 0.05)
    return price

# 다른 사람의 풀이
def solution2(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price*discount_rate)