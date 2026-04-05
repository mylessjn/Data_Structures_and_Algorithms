# Intuition
# My first thought was to use a counter that'd keep track of what point we are at in s while iterating through t and then using an if statement at the end to check if we reached our desired point and the counter equaled the length of the subsequence.

# Approach
# Practically we did the same thing as I described in my intuition but just made it cleaner. Using an while loop we had two indexes that kept track of where we were in each string, and using an if statement that checked if our current letter in t was equal to the one were looking for in s we'll iterate the counter for s forward as well. If s' pointer at some point reached the length of s then it'll return as true, else false.

# Complexity
# - Time complexity:
# O(n)

# - Space complexity:
# O(1)


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        p1 = 0
        p2 = 0
        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1
        if p1 == len(s):
            return True
        return False


