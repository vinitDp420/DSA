class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # nums2 =[]
        # for i in range(0,len(nums)):
        #     nums2.append(sum(nums[:i+1]))
        # return nums2
        nums2 = []
        for i in range(0,len(nums)):
            nums2.append(sum(nums[:i+1]))
        return nums2
