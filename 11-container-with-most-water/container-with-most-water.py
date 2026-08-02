class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0 
        right = n - 1
        max_con = 0
        while left < right:
            area = (right - left) * min(height[left] , height[right])
            if area > max_con:
                max_con = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_con
