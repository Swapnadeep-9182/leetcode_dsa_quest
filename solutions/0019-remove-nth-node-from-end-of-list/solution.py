# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        target_index = length - n
        current = dummy
        for _ in range(target_index):
            current = current.next
        current.next = current.next.next
        return dummy.next
