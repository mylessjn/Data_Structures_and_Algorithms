# Intuition
#First thought was to use breadth first search.

# Approach
#Implemented a greedy approach that basically was a manual breadth search that created a level using two pointers.

# Complexity
#- Time complexity:
#O(n)

#- Space complexity:
#O(1)

# Code
#```python []
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #breadth first search is the easiest method for shortest path questions 
        #this is a breadth first search approach for a 2d array
        l, r = 0, 0
        result = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i]) #sets the stage for our next "level" i + nums[i] is the index were currently on and where we can go
            l = r + 1
            r = farthest
            result += 1
        return result
        
            

        
#```