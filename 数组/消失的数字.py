'''
找到消失的数字，
给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。
请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。
'''

#用另一种形式的字典进行存储数据。
class Solution(object):
    def findDisappearedNumbers(self, nums):

        total_m=len(nums)
        list_q=[]
        list_i=[]
        for q in range(total_m):
            list_q.append(0)
        for i in nums:
            list_q[i-1]+=1
        for q,v in enumerate(list_q):
            if v ==0:
                list_i.append(q+1)
        return list_i
so=Solution()
print(so.findDisappearedNumbers([2,3,1,2,4]))


class Solution2:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        for num in nums:
            x = (num - 1) % n
            nums[x] += n

        ret = [i + 1 for i, num in enumerate(nums) if num <= n]
        return ret

#很巧妙的思路，数字本身就是索引，通过这种索引的方式，指引
# 索引上的数值加上特别大的数值n即可。
so=Solution2()
print(so.findDisappearedNumbers([2,3,1,2,4]))