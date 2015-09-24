class Solution(object):
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        :O(n) n**2
        """
        if len(prices) == 0:
            return 0
        profit = 0
        for i in range(len(prices)):
            high = prices[i]
            for j in range(i + 1,len(prices)):
                if prices[j] > high:
                    high = prices[j]
            if high - prices[i] > profit:
                profit = high - prices[i]
        return profit

        def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        : O(n) n
        """
        if len(prices) == 0:
            return 0
        max_diff = 0
        min = 0
        for i in range(len(prices)):
            if (prices[i] < prices[min]):
                min = i
            diff = prices[i] - prices[min]
            if(max_diff < diff):
                max_diff = diff
        return max_diff
