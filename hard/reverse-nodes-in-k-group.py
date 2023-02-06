from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"


class Solution:
    Flag = None

    def reverseN(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1:
            self.Flag = head.next
            return head
        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = self.Flag
        return last

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pass
