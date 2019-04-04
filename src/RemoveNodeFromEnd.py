from list_node import ListNode


class Solution(object):
    def removeNthFromEnd(self, head, n):
        tmp = head
        first = head
        second = head
        for x in range(n + 1):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return tmp


demo = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

ret = demo.removeNthFromEnd(head, 3)

print("After execute")

while ret:
    print(ret.val)
    ret = ret.next
