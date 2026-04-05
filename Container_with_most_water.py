# Intuition
My first thought was to use a nested loop and brute force the problem. After that I thought to make it more efficient using two pointers specifically one starting from the beginning and one at the end. With this I can iterate over the array slowly while keeping track of our current best value.

# Approach
I used a while loop to go until the two pointers interacted with eachother and moved the left one if it was less than the right pointer and vice versa, and returned the max at the end.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)
# Code

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l1 = 0
        l2 = len(height) - 1
        maxw = 0
        while l1 < l2:
            maxw = max(maxw, (l2 - l1) * min(height[l1], height[l2]))
            if height[l1] < height[l2]:
                l1 += 1
            else: l2 -= 1
        return maxw

