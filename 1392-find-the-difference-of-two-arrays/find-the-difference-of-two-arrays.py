class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        nums1set = set(nums1)
        nums2set = set(nums2)
        ans1 = set()
        ans2 = set()
        for n in nums1:
            if n not in nums2set:
                ans1.add(n)
        for n in nums2:
            if n not in nums1set:
                ans2.add(n)   
        return [list(ans1) , list(ans2)]


