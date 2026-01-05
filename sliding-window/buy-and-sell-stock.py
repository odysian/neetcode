from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Init pointers for dynamic sliding window
        l, r = 0, 1
        maxP = 0
        # While our r pointer is in bounds
        while r < len(prices):
            # If left(buying) < right(selling)
            if prices[l] < prices[r]:
                # Calc profit, check if its max
                prof = prices[r] - prices[l]
                maxP = max(maxP, prof)
            # Else, l moves to r and is new buy
            else:
                l = r
            # Right always moves
            r += 1
        return maxP
