'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
'''

#下面的方法感觉逻辑上都很好，合理！
class ListNode(object):
    def __init__(self, val=0, next=None):  #这里自动初始话了。
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        re = ListNode(0)    #这里对于List(0)可以直接赋值得到链表感觉还不错。
        r=re
        carry=0
        while(l1 or l2):
            x= l1.val if l1 else 0
            y= l2.val if l2 else 0   #细节截断补0，不然一个链表空了就很尴尬。
            s=carry+x+y         #注意每一次都要加上前面的数值
            carry=s//10
            r.next=ListNode(s%10)
            r=r.next
            if(l1!=None):l1=l1.next
            if(l2!=None):l2=l2.next  #细节，先判断再赋值
        if(carry>0):
            r.next=ListNode(1)
        return re.next