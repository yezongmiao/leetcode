"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

"""

"""自己写的，用栈的思想没错，但是在细节处理上有点问题，比如单数符号以及开头就是右边符号则会越界"""
class Solution(object):
    def isValid(self, s):
        result = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                result.append(i)
            elif i == ")":
                if result[-1] == "(":
                    result = result[0:-1]
            elif i == "}":
                if result[-1] == "{":
                    result = result[0:-1]
            else:
                if result[-1] == "[":
                    result = result[0:-1]

            print(result)
        if result == []:
            return True
        else:
            return False

'''
用字典封装起来的想法感受一下：
'''
class Solution2:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}  #这里有个小细节，很关键，直接避免了查表查不到的问题
        stack = ['?']
        for c in s:
            if c in dic: stack.append(c)
            elif dic[stack.pop()] != c: return False
        return len(stack) == 1   #这里有个小细节，很关键，




s="]]"
sol=Solution2()
print(sol.isValid(s))