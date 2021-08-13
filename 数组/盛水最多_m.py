'''

给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的
一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个
端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得
它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。

'''
#这道题目的核心在于论证双指针为什么能够得到全局的最优解。
#因此所有消去的状态的面积都 < S(i, j)<S(i,j)。通俗的讲，我们每次向内移动短板，
# 所有的消去状态都不会导致丢失面积最大值 。
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area=0
        left=0
        right=len(height)-1

        while left!=right:
            area=(right-left)*min(height[left],height[right])
            max_area=max(max_area,area)
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        return max_area
height = [2,3,4,5,18,17,6]
s=Solution()
print(s.maxArea(height))