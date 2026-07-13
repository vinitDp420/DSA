class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_pri = prices[0]
        max_pri = 0
        for i in prices:
            if i < min_pri:
                min_pri = i
            profit = i - min_pri
            max_pri = max(profit , max_pri)
        return max_pri







            



