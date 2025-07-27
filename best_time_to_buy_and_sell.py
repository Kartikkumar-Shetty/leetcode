from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_i = 0
        min_i = 0
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i]<prices[min_i]:
                profit = prices[max_i] - prices[min_i]
                if profit>max_profit:
                    max_profit = profit
                min_i = i
                max_i = i
                
            if prices[i]>prices[max_i]:
                max_i = i
                profit = prices[max_i] - prices[min_i]
                if profit>max_profit:
                    max_profit = profit
        return max_profit

print(Solution().maxProfit([7,6,4,3,1]))