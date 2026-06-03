from typing import List

# Two pointers tc n sc 1
def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP

#Dynamic Programming tc n sc 1
def maxProfit1(self, prices: List[int]) -> int:
    maxP = 0
    minBuy = prices[0]
    
    for sell in prices:
        maxP = max(maxP, sell-minBuy)
        minBuy = min(sell, minBuy)
    return maxP