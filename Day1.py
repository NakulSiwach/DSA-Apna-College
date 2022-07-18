# DAY 1  APNA COLLEGE SHEET

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast==slow:
                return True
        return False


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        curr = head
        prev = None
        while curr.next is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr.next = prev
        return curr


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        count = 1
        temp = head
        while temp.next is not None:
            temp = temp.next
            count += 1
        if n > count:
            return head
        elif n == count:
            return head.next
        temp = head
        for i in range(count - n -1):
            temp = temp.next

        temp.next = temp.next.next
        return head


MOD = 10**9+7

def multiplyTwoList(head1, head2):
    temp1 = head1
    num1 = 0
    while temp1 is not None:
        num1 = num1*10 + temp1.data
        temp1 = temp1.next

    temp2 = head2
    num2 = 0
    while temp2 is not None:
        num2 = num2 * 10 + temp2.data
        temp2 = temp2.next

    return (num1*num2)% MOD


class Solution:
    def compute(self, head):
        prev = None
        curr = head
        while curr.next is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr.next = prev

        head = curr
        max_till_now = curr.data
        while curr is not None and curr.next is not None:
            if curr.next.data < max_till_now:
                curr.next = curr.next.next
            else:
                max_till_now = max(max_till_now,curr.next.data)
                curr = curr.next

        curr = head
        prev = None
        while curr.next is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr.next = prev
        return curr


class Solution:
    def removeDuplicates(self, head):
        if head is None or head.next is None:
            return head
        temp = head
        d = {temp.data: 1}
        while temp.next is not None:
            if temp.next.data in d:
                temp.next = temp.next.next
            else:
                d[temp.next.data] = 1
                temp = temp.next
        return head


class Solution:
    def deleteNode(self, curr_node):
        curr_node.data = curr_node.next.data
        curr_node.next = curr_node.next.next