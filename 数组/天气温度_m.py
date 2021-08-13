'''
请根据每日 气温 列表 temperatures ，请计算在每一天需要等几天才会有更高的温度。
如果气温在这之后都不会升高，请在该位置用 0 来代替。
'''

#双重的循环查找会超出时间限制，这个是最简单的，找一个更牛逼的算法吧。
class Solution(object):
    def dailyTemperatures(self, temperatures):
        length_t=len(temperatures)
        if length_t==1:
            return [0]
        result=[]
        for i in range(0,length_t):
            flag=1
            for j in range(i+1,length_t):
                if temperatures[j]-temperatures[i]>0:
                    result.append(j-i)
                    flag=0
                    break
            if flag==1:
                result.append(0)
        return  result


class Solution2(object):
    def dailyTemperatures2(self, temperatures):
        answer = [0] * len(temperatures)
        stack = [0]
        for i in range(1, len(temperatures)):
            # 情况一和情况二
            if temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            # 情况三
            else:
                while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                    answer[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        return answer


class Solution3(object):
    def dailyTemperatures(self, temperatures):
        length_t=len(temperatures)
        result=[0]*length_t
        stack=[0]
        for i in range(1,length_t):   #关键是stack寸的是索引，可以直接把0存进去进而避免了list长度为1的时候的特殊处理。
            if temperatures[i]<=temperatures[stack[-1]]:
                stack.append(i)
            else:
                while len(stack)!=0 and temperatures[stack[-1]]< temperatures[i]:
                    result[stack[-1]]=i-stack[-1]
                    stack.pop()
                stack.append(i)
        return result




pric = [73,74,75,71,69,72,76,73]

so = Solution3()
print(so.dailyTemperatures(pric))