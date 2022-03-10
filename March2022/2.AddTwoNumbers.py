# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3=ListNode()
        temp=l3
        carry=0
        while l1 or l2:
            add=carry
            if l1 and l2:
                add+=(l1.val+l2.val)
                l1=l1.next
                l2=l2.next
            elif l1:
                add+=l1.val
                l1=l1.next
            elif l2:
                add+=l2.val
                l2=l2.next
            carry=add//10
            add=add%10
            temp.next=ListNode(add)
            temp=temp.next
        if carry:
            temp.next=ListNode(carry)
        return l3.next
            
