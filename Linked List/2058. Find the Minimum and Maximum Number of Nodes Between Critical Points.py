# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        current = head
        maximum = 0
        minimum = 1e9
        left = 0
        index = 1
        result = [-1, -1]

        while current.next and current.next.next:
            index += 1
            second  = current.next.val
            third = current.next.next.val
            if second > current.val and second > third or second < current.val and second < third:
                if left != 0:
                    minimum = min(minimum, index - left)
                    maximum = maximum + index - left
                left = index

            current = current.next

        if minimum != 1e9:
            result = [minimum, maximum]

        return result
        