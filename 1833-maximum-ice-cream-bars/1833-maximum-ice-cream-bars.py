from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maximum_cost = max(costs)
        frequency = [0] * (maximum_cost + 1)

        for cost in costs:
            frequency[cost] += 1

        bars_bought = 0

        for price in range(1, maximum_cost + 1):
            if frequency[price] == 0:
                continue

            if price > coins:
                break

            bars_to_buy = min(frequency[price], coins // price)
            bars_bought += bars_to_buy
            coins -= bars_to_buy * price

        return bars_bought