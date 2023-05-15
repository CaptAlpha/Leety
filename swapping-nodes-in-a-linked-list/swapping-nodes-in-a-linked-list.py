class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Find the length of the linked list
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        # Handle edge cases where k is out of range
        if k <= 0 or k > length:
            return head

        # Find the values of the nodes to be swapped
        temp1 = None
        temp2 = None
        counter = 1
        temp = head
        while temp:
            if counter == k:
                temp1 = temp
            if counter == length - k + 1:
                temp2 = temp
            temp = temp.next
            counter += 1

        # Swap the values of the nodes
        temp1.val, temp2.val = temp2.val, temp1.val

        return head
