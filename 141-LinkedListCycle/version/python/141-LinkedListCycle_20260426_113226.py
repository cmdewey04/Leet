# Last updated: 4/26/2026, 11:32:26 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        if not head:
10            return False
11        t = head
12        h = head.next
13        while t and h:
14            if t == h:
15                return True
16            t = t.next
17            if h.next:
18                h = h.next.next
19            else:
20                return False
21        return False