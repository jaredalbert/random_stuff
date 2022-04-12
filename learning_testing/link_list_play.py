# -*- coding: utf-8 -*-
"""
Created on Mon May 27 09:47:37 2019

@author: jaredalbert
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __str__(self):
        return (f'{self.val}, {self.next}')

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(None)
        carry = 0
        current = head
        while l1 or l2:
            total = 0
            if l1:
                total += l1.val
            if l2:
                total += l2.val
            total += carry
            carry = 1 if total >= 10 else 0
            current.next  = ListNode(total % 10)
            current = current.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
            print(f'carry: {carry}, total: {total}, current:{current}, head: {head}, head.next: {head.next}')
        if carry:
            current.next = ListNode(carry)
        return head.next
#[2,4,3]
#[5,6,4]   
n1, n2, n3 = ListNode(2), ListNode(4), ListNode(3)
n1.next = n2
n2.next = n3
l1=n1

m1, m2, m3  = ListNode(5), ListNode(6), ListNode(4)
m1.next = m2
m2.next = m3
l2 = m1

#s = Solution()
#print(s.addTwoNumbers(l1,l2))

llh = ListNode(None)
mem = llh
mem.next = ListNode(1)
mem = mem.next
mem.next = ListNode(2)
print(llh.next)

t = list()
z = t
z.append([1,2])
print(t)
