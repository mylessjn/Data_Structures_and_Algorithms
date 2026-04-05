# Intuition
# My first thoughts were to try and figure out a way we could keep track of the count of a value appearing in the array without losing the old one. This then lead to a dictionary being the easiest solution to keep track of all of the values counts.

# Approach
# Create a loop that adds a key to a dictionary with the value being the count and it gets incremented every time we see the value again in the loop. Its 
# the same as the last solution it just uses a running leader to lower the complexity

# Complexity
# - Time complexity:
# O(n)

# - Space complexity:
# O(n)

# Code
# ```python []
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majorityelement = {}

        for i in range(len(nums)):

            if nums[i] not in majorityelement:
                majorityelement[nums[i]] = 1
            else:
                majorityelement[nums[i]] += 1
        return max(majorityelement, key=majorityelement.get)
                
# ```