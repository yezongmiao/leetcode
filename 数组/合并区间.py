'''
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
'''


#先进行排序可以锁定一个边界，这种情况就很有优势，方便进行后续
class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0])  #这个语法可以使用！很关键。
        merge=[]
        for i in intervals:
            if not merge or merge[-1][-1]<i[0]:
                merge.append(i)
            else:
                merge[-1][-1]=max(merge[-1][-1],i[-1])
        return merge