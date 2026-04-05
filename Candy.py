# Intuition
#My initial thought I wrote down was that if ratings [i] is greater than ratings[i+1] and ratings[i-1] it has to be greater than the bigger one by only +1. 

# Approach
#This can be done with a two pass approach which uses two loops and adds difference of the new amount of candy and old amount to the total sum. I also kept track of it through a list which can use the sum() to save time and space, I just wasn't aware of it while doing this problem.

# Complexity
#- Time complexity:
#O(n)

#- Space complexity:
#O(n)

# Code
#```python []
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        intanswer = 0 + (1 * len(ratings))
        answer = [1 for num in ratings]
        if len(ratings) == 1: return 1
        elif len(ratings) == 0: return 0 #edge cases

        for i in range(len(ratings) - 1):
            if ratings[i] > ratings[i+1] and answer[i] <= answer[i+1]:

                intanswer += (answer[i+1] + 1) - answer[i]
                answer[i] = answer[i + 1] + 1

            elif ratings[i+1] > ratings[i] and answer[i+1] <= answer[i]:

                intanswer += (answer[i] + 1) - answer[i+1]
                answer[i+1] = answer[i] + 1

        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i] > ratings[i - 1] and answer[i] <= answer[i-1]:

                intanswer += (answer[i - 1] + 1) - answer[i-1]

                answer[i] = answer[i - 1] + 1
            elif ratings[i - 1] > ratings[i] and answer[i - 1] <= answer[i]:

                intanswer += (answer[i] + 1) - answer[i-1]

                answer[i - 1] = answer[i] + 1

        print answer
        return intanswer
        


#```