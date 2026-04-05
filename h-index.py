# Intuition
#I thought I would keep track of h-values in a dictionary and iterate through it backwards with a counter until that counter found a valid h-index to return

# Approach
#create a dictionary that keeps tracking of the values up the the length of citations then use another loop that breaks when it i reaches 0, which returns 0. It'll return the first valid h-index which is the biggest one before it reaches that point if it has a valid index.

# Complexity
#- Time complexity:
#O(n)

#- Space complexity:
#O(n)

# Code
#```python []
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        #basically want to find for h amount of papers are there h amount of citations atleast? the highest amount of citations given on h papers so if there were 8 papers and atleast 5 of them had 5 citations that would make the h index 5
        mydict = {i+1:0 for i in range(len(citations))}

        for i in range(len(citations)):
            if citations[i] >= len(citations):
                mydict[len(citations)] += 1
            elif citations[i] == 0:
                continue
            else:
                mydict[citations[i]] += 1

        valid_numbers = 0
        index = len(citations)
        while(index > 0):
            valid_numbers += mydict[index]
            if valid_numbers >= index:
                return index
            index -= 1

        return 0

        print mydict

#```