import numpy as np

prices = np.array([100, 200, 300])
print(prices + 50)
print(prices * 2)
print(prices - 10)
print(prices / 100)

prices = np.array([100, 200, 300])
quantities = np.array([2, 1, 3])
totals = prices * quantities
print(totals)

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(list_a + list_b)
print(np.array(list_a) + np.array(list_b))

#practical
prices_arr=np.array([100, 250, 400])
qty_arr=np.array([2,1,3])
cost=prices_arr*qty_arr
print(cost)
with_deleivery_fee=cost+50
print(with_deleivery_fee)
print([100, 250] + [50])