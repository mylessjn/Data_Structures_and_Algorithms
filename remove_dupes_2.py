class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #nums is sorted in least to greatest order. Remove duplicates and only allow a duplicate to appear at most twice. keep the order the same.
        #new list will be the index of the numbers that'll be moved to the end pushed by variable temp.
        moving_list = []

        for i in range(len(nums) - 2):

            if nums[i + 2] == nums[i]:
                temp = i + 2
                moving_list.append(temp)
            i += 1

        for j in range(len(moving_list)):
            moving_list_curr = moving_list[j]
            nums[moving_list_curr] = 1000001
        nums.sort()
        k = len(nums) - 1
        i = 0
        while i < len(moving_list):
            nums.pop(k)
            k -= 1
            i += 1
        print(moving_list)
        return k + 1
