class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = 0
        counter = 0
        s = ''
        temp = head
        while temp is not None:
            s+=(str(temp.val))
            temp = temp.next
        return int(s, 2)
