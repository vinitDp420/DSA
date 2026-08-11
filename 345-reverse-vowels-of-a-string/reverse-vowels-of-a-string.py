class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        vowels = "aeiouAEIOU"
        slist = list(s)
        left = 0
        right = n-1
        while left < right:
            while left < right and slist[left] not in vowels:
                left += 1
            while left < right and slist[right] not in vowels:
                right -= 1
            if left < right:
                slist[left], slist[right] = slist[right], slist[left]
                left += 1
                right -= 1
        return "".join(slist)
        
