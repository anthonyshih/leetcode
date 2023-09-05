"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


"""

def maxProfit(self, prices):
        if not prices:
            return 0  # 處理空清單的情況，直接回傳0

        max_profit = 0
        min_price = prices[0]

        for price in prices:
            if price < min_price:
                min_price = price  # 如果遇到更低的價格，則更新最低價格
            else:
                profit = price - min_price  # 計算以當前價格出售的利潤
                max_profit = max(max_profit, profit)  # 更新最大利潤

        return max_profit

prices = [7,6,4,3,1]
print(max_profit(prices))
