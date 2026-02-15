# Intuition
#At first I heavily overthought it but you can just brute force it by adding the profits of prices[i+1] - prices[i] if prices i is less than prices i + 1

# Approach
#made a loop that checked if the next index is greater than our current, and added the profit to the current profit it is.

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
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i+1]:
                profit += (prices[i+1] - prices[i])
            else:
                continue
        return profit

#```