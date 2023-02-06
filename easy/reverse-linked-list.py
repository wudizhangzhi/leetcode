from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if head.next == None:
            return head
        last = self.reverseList(head.next)
        print(head, last)
        head.next.next = head  # 当前节点的下一个，指向自己
        head.next = None  # 当前节点指向空
        return last

    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head:
    #         return head
    #     pre = None
    #     cur = head
    #     while cur != None:
    #         next = cur.next
    #         cur.next = pre
    #         pre, cur = cur, next
    #     return pre


if __name__ == "__main__":
    nodes = ListNode(
        1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5))))
    )
    res = Solution().reverseList(nodes)
    while res:
        print(res.val)
        res = res.next
