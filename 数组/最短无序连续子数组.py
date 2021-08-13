'''
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
'''


#通过了我靠，一个双指针磕磕巴巴，我醉了。
class Solution(object):
    def findUnsortedSubarray(self, nums):
        forward_cur=0
        backward_cur=len(nums)-1
        if backward_cur==0:return 0
        while forward_cur<backward_cur :
            left_flag=0
            right_flag=0
            max_=max(nums[forward_cur:backward_cur+1])
            min_=min(nums[forward_cur:backward_cur+1])
            if min_>=nums[forward_cur]:
                forward_cur+=1
                left_flag=1
            if max_<=nums[backward_cur]:
                backward_cur-=1
                right_flag=1
            if left_flag ==0 and right_flag==0:
                break
        if backward_cur-forward_cur ==0:
            return 0
        return backward_cur-forward_cur+1

s=Solution()
print(s.findUnsortedSubarray([1,2,4,5,6]))



