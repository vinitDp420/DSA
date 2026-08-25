class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maxcount = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                maxcount = max(count , maxcount)  
                count = 0
        return max(count, maxcount)