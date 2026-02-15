# Intuition
#Keep a running lowest amount and update it everytime the current index of prices is lower than the old lowest amount. We'll also update the max profit whenever the current index of prices is greater than the old max profit, and since it's initialized at 0 it'll return 0 if its never updated.

# Approach
#Make a for loop the iterates n times that keeps track of the lowest amount and uses that to calculate the max profit.

# Complexity
#- Time complexity:
#O(n)

#- Space complexity:
#O(1)

# Code
#```python []
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest_price = prices[0]
        max_profit = 0
        for i in range(len(prices)):

            if prices[i] < lowest_price:
                lowest_price = prices[i]
            curr_profit = prices[i] - lowest_price
            if max_profit < curr_profit:
                max_profit = curr_profit
                
        return max_profit

#```