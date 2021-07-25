import numpy as np

class Solution(object):           #最简单的双指针从头开始。
    def twoSum(self, nums, target):
        l_nums= len(nums)
        print(l_nums)
        for i in range(l_nums-1):
            for j in range(i+1,l_nums):
                if (target==nums[i]+nums[j]):
                    return [i,j]

class Solution1(object):           #最简单的双指针从头开始。
    def twoSum(self, nums, target):
        l_nums= len(nums)
        dict_unput={}
        for i in range(l_nums):
            dict_unput[nums[i]]=i
        for q in range(l_nums):
            p=dict_unput.get(target - nums[q])
            print(p,q)
            if( p and q!=p):
                return [q,p]

class Solution2(object):           #最简单的双指针从头开始。
    def two_sum(nums, target):
        """这样写更直观，遍历列表同时查字典"""
        dct = {}
        for i, n in enumerate(nums):
            cp = target - n
            if cp in dct:
                return [dct[cp], i]
            else:
                dct[n] = i


testlis=[3,2,4]
sol=Solution1()
print(sol.twoSum(testlis,target=6))