class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        left = 0
        right = n - 1
        max_count = 0
        while left < right:
            if nums[left] + nums[right] == k:
                left += 1
                right -= 1
                max_count += 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1
        return max_count