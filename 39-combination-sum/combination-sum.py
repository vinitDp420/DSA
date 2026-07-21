class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        def backtrack(start,path):
            if sum(path) == target:
                result.append(path[:])
                return 
            if sum(path) > target:
                return 

            for i in range(start , len(candidates)):
                path.append(candidates[i])
                backtrack(i,path)
                path.pop()
        backtrack(0,[])
        return result