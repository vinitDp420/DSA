class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        mi = nums.index(m)
        for i,num in enumerate(nums):
            if i != mi and m < 2*num:
                return -1
        return mi