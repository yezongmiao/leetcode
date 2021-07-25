"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
"""

'''
好吧超出了时间限制，实际上max函数内部估计是调用了循环叭。
'''
class Solution(object):
    def maxProfit(self, prices):
        max_=-1
        for idx, i in enumerate(prices):
            max2=max(prices[idx:])
            max_=max(max_,max2-i)
        return max_

"""
看看方案二，今晚先不看了吧不然。
"""


pric = [7,6,4,3,10]
so=Solution()
print(so.maxProfit(pric))