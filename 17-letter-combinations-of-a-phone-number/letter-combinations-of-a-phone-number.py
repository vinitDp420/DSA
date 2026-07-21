class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []
        def backtrack(start , path):
            if start == len(digits):
                result.append(path)
                return 
            curr_digit = digits[start]
            letters = mapping[curr_digit]
            for i in letters:
                
                backtrack(start+1,path + i)
                
        backtrack(0,"")
        return result