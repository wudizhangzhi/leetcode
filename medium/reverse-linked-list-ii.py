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

    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head:
            return head
        if left == 1:
            return self.reverseN(head, right)
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head

    def reverseN(self, head: Optional[ListNode], n: int):
        if n == 1:
            self.Flag = head.next
            return head
        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = self.Flag
        return last


if __name__ == "__main__":
    nodes = ListNode(
        1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5))))
    )
    res = Solution().reverseBetween(nodes, 2, 3)
    # res = Solution().reverseN(nodes, 2)
    print(res)
