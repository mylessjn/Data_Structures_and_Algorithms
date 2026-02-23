# Intuition
# At first I brute forced the problem using an O(n^2) solution but understanding that we just need a respective points lowest bar on one side because it'll let us ignore the bars between the right highest and left lowest if the left was the index were testing.

# Approach
#Use two points that loop until the meet each other, and it checks either the left or right index depending on whats smaller

# Complexity
#- Time complexity:
#O(n)

#- Space complexity:
#O(1)

# Code
#```python []
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """ #shortest - height
        l, r = 0, len(height) - 1
        leftbar = height[l]
        rightbar = height[r]
        water = 0
        while (l<r):
            if leftbar < rightbar:
                leftbar = max(leftbar, height[l])
                l += 1
                if (leftbar - height[l]) >= 0:
                    water += (leftbar - height[l])
                leftbar = max(leftbar, height[l])
            else:
                rightbar = max(rightbar, height[r])
                r -= 1
                if (rightbar - height[r]) >= 0:
                    water += (rightbar - height[r])
                rightbar = max(rightbar, height[r])
        return water

#```