class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            minprice = min(minprice, prices[i])
            ans = max(ans, prices[i] - minprice)
        return ans
