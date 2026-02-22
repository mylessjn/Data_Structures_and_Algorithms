# Intuition
#You dont have to import random since this is leetcode but you I just assumed I'd be using it for this problem. The other parts were intuitive the only restraint was that it had to be O(1). To complete this, I had to use a dictionary and list so I can easily search through a list with a stored index in dictionary so I wouldn't have to go through the entire thing.

# Approach
#Use both a list and dictionary to fill in each others weak points and achieve O(1) complexity by storing indexes that from the list in the dictionary, and the list to easily get rid of the values.

# Complexity
#- Time complexity:
#O(1)

#- Space complexity:
#O(1)

# Code
#```python []
class RandomizedSet(object):

    def __init__(self):
        self.data_list = []
        self.data_map = {}
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.data_map:
            self.data_map[val] = len(self.data_list)
            self.data_list.append(val)
            return True
        else: return False
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.data_map:
            remove_index = self.data_map[val]
            last_value = self.data_list[len(self.data_list) - 1]
            self.data_list[remove_index] = last_value
            self.data_map[last_value] = remove_index
            self.data_list.pop()
            
            del self.data_map[val]
            return True



        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.data_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
#```