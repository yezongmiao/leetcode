'''
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
'''

#这个是单指针，还有双指针好像很强。
class Solution(object):
    def sortColors(self, nums):
        lg=len(nums)
        id0=0
        id1=0
        id2=0
        i=0
        while i<lg-id2:
            if nums[i]==0:
                nums[i],nums[id0]=nums[id0],nums[i]
                id0+=1
            if nums[i]==2:
                nums[i],nums[lg-1-id2]=nums[lg-1-id2],nums[i]
                id2+=1
                i-=1
            i+=1
        return nums

s=Solution()
print(s.sortColors(
[0,1,0]))