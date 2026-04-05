# Intuition
#I thought to first translate it to binary by using a list and comparing each bit to 1, then using count to decide which pointer we move and just giving the biggest difference between the two pointers.

# Approach
#created a 32 bit list of integers to hold the value in binary then iterated over it keeping track of ones using pointers then finding the biggest difference between them.

# Complexity
#- Time complexity:
#O(1)

#- Space complexity:
#O(1)

# Code
#```python []
class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        longest = 0
        indexed = [(n>>i) & 1 for i in range(31, -1, -1)]
        l, r, = 0, 0
        count = 0
        for i in range(len(indexed)): # lets use a two pointer approach
            if indexed[i] == 1:
                count += 1
            if count % 2 == 1 and indexed[i] == 1: l = i #move left pointer
            elif count % 2 == 0 and indexed[i] == 1: r = i # move right pointer
            if count > 0 and r != 0:
                longest = max(longest, r - l, l - r)

        return longest



#```