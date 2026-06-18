# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findMiddle(self, head):
        if head is None:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head):
        if head is None:
            return None
        prev = None
        curr = head 
        while curr:
            nxt = curr.next 
            curr.next = prev
            prev = curr
            curr = nxt 
        return prev 

    def combine(self, head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1

        temp1 = head1
        temp2 = head2
        while temp1 and temp2:
            t1 = temp1.next
            t2 = temp2.next
            temp1.next = temp2
            temp2.next = t1
            temp1 = t1
            temp2 = t2

        return head1

    def reorderList(self, head: Optional[ListNode]) -> None:
        middle = self.findMiddle(head)
        temp = middle.next
        middle.next = None
        head1 = head
        head2 = temp
        head2 = self.reverse(head2)
        head = self.combine(head1, head2)
        return 
        