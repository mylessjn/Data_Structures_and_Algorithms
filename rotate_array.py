# Intuition
#Brute force it, pop the last element then insert it. 
# Approach
#Tried brute forcing it, exceeded time limit for a test case. Switching to slicing to do all of the movements at once rather than within a loop
# Complexity
#- Time complexity:
#O(n)

#- Space complexity:
#O(1)

# Code
#```python []
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        i = 0
        print(k)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]

        
#```