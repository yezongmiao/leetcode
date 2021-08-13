'''

给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。


'''

#

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        min_k=0
        resutl=[]
        if len(nums)<3:
            return  []
        if nums[-3:]==[0,0,0]:
            return [0,0,0]
        while nums[min_k]<=0:      #没办法处理特殊情况[0,0,0]结尾的。
            if min_k==0:
                print("111")
            else:
                if nums[min_k] == nums[min_k - 1]:
                    min_k += 1
                    continue

            for i in range(min_k+1,len(nums)):
                for j in range(i+1,len(nums)):
                    if(nums[min_k]+nums[i]+nums[j]==0):
                        resutl.append([nums[min_k],nums[i],nums[j]])
            min_k += 1
        return resutl


class Solutio1n:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()
        res, k = [], 0
        for k in range(len(nums) - 2):   #这里小设计就避免了while的问题，nice
            if nums[k] > 0: break # 1. because of j > i > k.
            if k > 0 and nums[k] == nums[k - 1]: continue # 2. skip the same `nums[k]`.
            i, j = k + 1, len(nums) - 1    #双指针，一头一尾，可以避免组内重复访问，niube
            while i < j: # 3. double pointer
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
        return res

height = [0,0,0]  [-1,0,1,0] #后面这个也没办法去重复啊西、

s=Solution()
print(s.threeSum(height))