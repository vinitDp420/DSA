class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n==1: return 1
        # if n==2: return 2
        # p1=1
        # p2=2
        # for i in range(3,n+1):
        #     curr = p1+p2
        #     p2=p1
        #     p1=curr
        # return curr


        # if n<=2 : 
        #     return n
        # dp = [0]*(n+1)
        # dp[1]=1
        # dp[2]=2
        # for i in range(3,n+1):
        #     dp[i]=dp[i-1] + dp[i-2]
        # return dp[n]

        if n<=2:
            return n
        dp = [0]*(n+1)
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        
        