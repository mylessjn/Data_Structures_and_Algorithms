# Intuition
#I first thought to create a manual adder using a dictionary to skip the if statements .

# Approach
#first made sure both strings were the same length by filling the smaller one with zeroes and then I used a loop that added to the dictionary and carried over an extra ones. Once the dictionary is finished using another loop that iterates through it backwards add it to the string sum then return it

# Complexity
#- Time complexity:
# O(n)

#- Space complexity:
#O(n) 

# Code
#```python []
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        adder = defaultdict(int)
        sum = ""
        if len(a) > len(b):
            longer_s = a
            b = b.zfill(len(a))
        else:
            longer_s = b
            a = a.zfill(len(b))

        for i in range(len(longer_s)):

            adder[i] += (int(a[len(a) - (i + 1)]) + int(b[len(b) - (i + 1)]))

            if adder[i] > 1:
                adder[i] -= 2
                adder[i+1] += 1
        
        for i in range(len(adder) - 1, -1, -1):
            sum += str(adder[i])
        return sum
#```