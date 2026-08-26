class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = []
        for num in nums:
            result.append(num * num)
        return sorted(result)
    
        
        # left = 0
        # right = n-1
        # while right > left:
        #     if right[i] > left[i]:
        #         right+=1
        #     else:
        #         left+=1
            
        