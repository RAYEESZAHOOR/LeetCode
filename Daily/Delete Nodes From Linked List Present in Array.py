# You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        max_val = -1
        for num in nums:
            max_val = max(num, max_val)

        freq = [False] * (max_val + 1)

        for num in nums:
            freq[num] = True

        temp = ListNode()
        current = temp

        while head:
            if head.val >= len(freq) or not freq[head.val]:
                current.next = head
                current = current.next
            head = head.next

        current.next = None

        return temp.next

        