# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        r={}
        while temp!=None:
            if temp.val not in r:
                r[temp.val]=1
            else:
                r[temp.val]+=1
            temp=temp.next
        
        # print(r)
        dummy=ListNode()
        temp2=dummy
        temp=head
        while temp!=None:
            # print(temp.val)
            if r[temp.val]==1:
                temp2.next=ListNode(temp.val)
                # print(temp2)
                temp2=temp2.next
            temp=temp.next
        return dummy.next
