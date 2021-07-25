"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
这道题目好像并不是easy的？
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
         """
        for i in range(1, len(nums)):
            nums[i]= nums[i] + max(nums[i-1], 0)
        return max(nums)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
so=Solution()
print(so.maxSubArray(nums))