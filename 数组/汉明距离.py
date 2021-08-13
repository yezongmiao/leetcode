'''
两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。

给你两个整数 x 和 y，计算并返回它们之间的汉明距离。
'''


class Solution(object):
    def hammingDistance(self, x, y):
        q=x^y
        sum=0
        while q!=0:
            sum+=q%2
            q=int(q/2)
        return sum
so=Solution()
print(so.hammingDistance(3,1))
