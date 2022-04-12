#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
            self.val = x
            self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        out = ListNode(0)
        remainder = 0
        
        out.val = (int(l1.val) + int(l2.val))
        #remainder =  (l1.val + l2.val)%10
        return (type(out.val))

l1 =ListNode([2,4,3])
l2 = ListNode([5,6,4])
#
#s = Solution()
#print(s.addTwoNumbers(l1,l2))
#
#class Solution:
#    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#        out = ListNode(0)
#        remainder = 0
#        head = 0
#        if l1 and l2:
#            if (int(l1.val) + int(l2.val))//10 == 0:
#                out.val = (int(l1.val) + int(l2.val))
#            else:
#                out.val = (int(l1.val) + int(l2.val))%10
#                remainder = (int(l1.val) + int(l2.val))//10
#        
#        return remainder, out.val
head = None
current = head
current = 1
