'''
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数
'''


#前缀和的思路，但是超时了，通过字典的形式可以少一次循环，这样就不用超时了。
class Solution(object):
    def subarraySum(self, nums, k):
        lenght_nums=len(nums)
        result=[0]
        r_index=0
        if lenght_nums==1 and nums[0]==k:
            return 1
        for i in range(lenght_nums):
            result.append(sum(nums[0:i+1]))
            for q in range(i+1):
                if result[i+1]-result[q]==k:
                    r_index+=1
        return r_index

from collections import Counter


#字典的形式，Counter就是字典么，但是感觉需要字典很大啊。
class Solution2:
    def subarraySum(self, nums, k):
        dic = Counter({0: 1})    #这部分是初始化为0么
        ret = pre_sum = 0
        for i in nums:
            pre_sum += i
            ret += dic[pre_sum - k]
            dic[pre_sum] += 1
        return ret

s=Solution()
print(s.subarraySum([1,2,3],k=3))

dic = Counter({0: 1})

print(dic[1])