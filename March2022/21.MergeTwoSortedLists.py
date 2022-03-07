class Solution:
    #l1 and l2 are two objects of listnode  class
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        head = cur = ListNode()#head and cur are two objects of listnode class
        while l1 or l2:
            if not l1:
                cur.next = l2
                return head.next
            if not l2:
                cur.next = l1
                return head.next
            if l2.val < l1.val:
                cur.next = ListNode(l2.val)
                l2 = l2.next if l2 else None
            else:
                cur.next = ListNode(l1.val)
                l1 = l1.next if l1 else None
            cur = cur.next
        return head.next
        
