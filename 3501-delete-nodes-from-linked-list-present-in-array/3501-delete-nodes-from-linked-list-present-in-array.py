# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        while head and head.val in nums:
            head = head.next
        prev = head
        current = prev.next
        while current:
            if current.val in nums:
                prev.next = current.next
                current = prev.next
            else:
                prev = prev.next
                current = current.next
        return head