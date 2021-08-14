'''
给定一个包含非负整数的 m x n 网格 grid ，
请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
'''

#理论上是可以用的，但是好像是二维的list创建的问题，导致好像数值的地址是一样的
# print(id(arrs[0]), id(arrs[1])) 验证了地址是一样的  淦
class Solution(object):
    def minPathSum(self, grid):
        hang=len(grid)
        lie=len(grid[0])

        #开始边界条件。
        arr=[0]*lie
        arrs=[arr]*hang
        sum=0
        for i in range(lie):
            sum+=grid[0][i]
            arrs[0][i]=sum
        sum = 0
        for q in range(hang):
            sum+=grid[q][0]
            arrs[q][0]=sum

        print(id(arrs[0]),id(arrs[1]))
        for i in range(1,hang):
            for j in range(1,lie):
                arrs[i][j]=min(arrs[i-1][j],arrs[i][j-1])+grid[i][j]
        return arrs[hang-1][lie-1]

class Solution2:
    def minPathSum(self, grid: [[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0: continue
                elif i == 0:  grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:  grid[i][j] = grid[i - 1][j] + grid[i][j]
                else: grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]

s=Solution()
grid = [[7,4,8,7,9,3,7,5,0],[1,8,2,2,7,1,4,5,7],[4,6,4,7,7,4,8,2,1],[1,9,6,9,8,2,9,7,2],[5,5,7,5,8,7,9,1,4],[0,7,9,9,1,5,3,9,4]]
print(s.minPathSum(grid))