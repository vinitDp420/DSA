class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #First approach
        # n = len(nums)
        # result = []
        # for num in nums:
        #     result.append(num * num)
        # return sorted(result)
    
        n=len(nums)
        result = [0] * n
        left = 0
        right = n-1
        pos = n-1
        while left <= right:
            left_sq = nums[left] ** 2
            right_sq = nums[right] ** 2
            if left_sq > right_sq:
                result[pos] = left_sq
                left += 1
                
            else:
                result[pos] = right_sq
                right -= 1
            pos -= 1
                
        return result
            
        