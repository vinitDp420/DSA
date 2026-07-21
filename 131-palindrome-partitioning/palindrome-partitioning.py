class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []

        def ispalindrome(s):
            return s == s[::-1]
        
        def backtrack(start , path):
            if start == len(s):
                return result.append(path[:])
                return 
            for end in range(start + 1 , len(s)+1):
                substring = s[start:end]
                if ispalindrome(substring):
                    path.append(substring)
                    backtrack(end , path)
                    path.pop()
        backtrack(0,[])
        return result
        