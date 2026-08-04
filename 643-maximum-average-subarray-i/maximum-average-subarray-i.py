class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum = 0
        for i in range(k):
            sum += nums[i]
        max_sum = sum
        for i in range(k , len(nums)):
            sum += nums[i] - nums[i-k]
            max_sum = max(max_sum , sum)
        return float(max_sum) / k
