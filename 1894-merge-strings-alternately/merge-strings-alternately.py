class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        n1 = len(word1)
        n2 = len(word2)
        i,j=0,0
        while i < n1 or j < n2:
            if i < n1:
                result.append(word1[i])
                i += 1
            if j < n2:
                result.append(word2[j])
                j += 1
        return "".join(result)
        
                

        