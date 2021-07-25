# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
'''

'''
通过迭代的想法，对比两个支路的指针大小，如果哪个小，就指向哪个。
'''
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        prehead=ListNode(-1)
        pre=prehead
        while l1 and l2:
            if l1.val<=l2.val:
                pre.next=l1
                l1=l1.next
            else:
                pre.next=l2
                l2.next=l2
            pre=pre.next
        pre.next=l1 if l1 is None else l2
        return prehead

class Solution1(object):
    def mergeTwoLists(self, l1, l2):
        prehead=ListNode(-1)
        pre=prehead
        while l1 and l2:
            if l1.val<=l2.val:
                pre.next=l1
                l1=l1.next
            else:
                pre.next=l2
                l2.next=l2
            pre=pre.next
        pre.next=l1 if l1 is None else l2
        return prehead
