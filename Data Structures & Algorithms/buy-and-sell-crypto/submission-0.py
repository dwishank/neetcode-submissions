class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        profit = 0
        buy = prices[0]

        maxprofit = 0 
        listlen = len(prices)

        for i in prices[1:]:
            if(i > buy):
                profit = i - buy
                print(profit)
                if(maxprofit < profit):
                    maxprofit = profit
            else:
                buy = i
            
        return(maxprofit)

            