def total_price(prices, discount):
    total = 0
    for price in prices:
        total = total+price
    return total - discount


print(total_price([100, 200, 300], 50))
