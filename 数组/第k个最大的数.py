'''

给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。


'''

#简单的选择排序算法。 这不就是字节的面试题目吗  干！！！！！md

#top_k的算法，
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/ji-yu-kuai-pai-de-suo-you-topkwen-ti-jia-ylsd/
class Solution(object):
    def findKthLargest(self, nums, k):
        nums_lenght=len(nums)
        if nums_lenght==1:
            return nums[0]
        for i in range(0,k):
            for q in range(i+1,nums_lenght):
                if nums[i]<=nums[q]:
                    nums[i],nums[q]=nums[q],nums[i]
        return nums[k-1]


height = [3,2,1,5,6,4]   #后面这个也没办法去重复啊西、

s=Solution()
print(s.findKthLargest(height,2))