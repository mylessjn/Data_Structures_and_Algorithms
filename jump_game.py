# Intuition
#My initial thought was to just brute force it by decrementing the jump until it hits 0 and using some ifs to check when we hit our goal or not and some edge cases.1

# Approach
#I used a while loop that returned false when we've exhausted every single possible jump and returned true if it ever passed len(nums) - 1 or equaled it. This was tricky because of the index error but was easily fixable using a try function.

# Complexity
#- Time complexity:
#O(n^2)

#- Space complexity:
#O(1)

# Code
#```python []
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #lets go through every single possible solution. I can do this by using the range of each integer
        #from 1 to int and if a jump leads to a 0 it back tracks and trys the next possible output until it
        #runs out 
        current_index = 0
        if(current_index == len(nums) - 1):
            return True
        while(True):
            temp = current_index


            if (nums[0] == 0): # no more possible jumps
                return False

            if (nums[current_index] == 0 and current_index != len(nums) - 1):
                current_index -= 1
                continue   #we modify indexes since the jump is directly coorelated to how many spots we jump

            temp += nums[current_index]
            
            try:

                if (nums[temp] == 0 and temp != len(nums) - 1): #the jump will lead to a dead end
                    nums[current_index] -= 1
                    temp = nums[current_index]
                    continue
            except IndexError:
                return True

            current_index = temp

            if (current_index >= len(nums) - 1):
                return True


            
            
#```