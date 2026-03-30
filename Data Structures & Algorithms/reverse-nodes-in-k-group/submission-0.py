class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        values = []
        curr = head

        while curr:
            values.append(curr.val)
            curr = curr.next
        
        nodes = []
        for i in range(0, len(values), k):
            group = values[i:i+k]
            if len(group) == k:
                nodes.extend(group[::-1])
            else:
                nodes.extend(group)
        dummy = ListNode(0)
        curr = dummy
        for val in nodes:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next