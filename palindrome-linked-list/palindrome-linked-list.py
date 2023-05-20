# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        flag = 0
        li = []
        end = 0
        while(temp is not None):
            li.append(temp.val)
            temp = temp.next

        return li == li[::-1]

        


        