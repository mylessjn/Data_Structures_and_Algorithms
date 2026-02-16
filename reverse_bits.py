# Intuition
#My first thought was to convert the entire n from decimal to binary then reverse the entire thing because I didn't realize you could do bitwise operations, but after some research and reading I was able to find a much more efficient path.

# Approach
#I just used a for loop that took the last int in n and then pushed it to versed which is what were going to return. then I'd shift n to the right which allowed us to get the next number to use in the loop without having to iterate through it.

# Complexity
#- Time complexity:
#O(1)

#- Space complexity:
#O(1)

# Code
#```python []
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        versed = 0
        for int in range(32):
            versed <<= 1
            versed = versed + (n & 1)
            n >>= 1
        return versed
#```