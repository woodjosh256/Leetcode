from typing import Any, List, Optional

"""
Reorder Linked List
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

Example 1:

Input: head = [2,4,6,8]

Output: [2,8,4,6]
Example 2:

Input: head = [2,4,6,8,10]

Output: [2,10,4,8,6]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def make_from_list(arr: List[Any]):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for i in range(1, len(arr)):
            current.next = ListNode(arr[i])
            current = current.next
        return head

    def __eq__(self, head):
        current = self
        while head:
            if current.val != head.val:
                return False
            current = current.next
            head = head.next
        return True

    def __str__(self):
        current = self
        arr = []
        while current:
            arr.append(current.val)
            current = current.next
        return str(arr)


class Solution:

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = None
        while head:
            next = head.next
            head.next = last
            last = head
            head = next

        return last

    def get_length(self, head: Optional[ListNode]) -> int:
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def remove_nth_from_end(self, head: Optional[ListNode], n) -> None:
        right = head
        for _ in range(n):
            right = right.next
        left = None
        while right:
            right = right.next
            if left is None:
                left = head
            else:
                left = left.next
        if left is None:
            head = head.next
        else:
            left.next = left.next.next

        return head


    def reorderList(self, head: Optional[ListNode]) -> None:
        length = self.get_length(head)

        pos = 0
        current = head
        last = None
        while current and pos < length / 2:
            last = current
            current = current.next
            pos += 1
        if last:
            last.next = None

        reversed = self.reverse_list(current)

        current = head
        while reversed:
            next = current.next
            inserted = reversed
            reversed = reversed.next
            current.next = inserted
            inserted.next = next
            current = current.next.next
        return head





def test_case_1():
    head = ListNode.make_from_list([2, 4, 6, 8])
    expected = ListNode.make_from_list([2, 8, 4, 6])
    s = Solution()
    reordered = s.reorderList(head)
    print(f"Test case 1. Expected: {expected}, got: {reordered}")


def test_case_2():
    head = ListNode.make_from_list([2, 4, 6, 8, 10])
    expected = ListNode.make_from_list([2, 10, 4, 8, 6])
    s = Solution()
    reordered = s.reorderList(head)
    print(f"Test case 2. Expected: {expected}, got: {reordered}")

def test_case_3():
    head = ListNode.make_from_list([])
    expected = ListNode.make_from_list([])
    s = Solution()
    reordered = s.reorderList(head)
    print(f"Test case 3. Expected: {expected}, got: {reordered}")

if __name__ == '__main__':
    test_case_1()
    test_case_2()
    test_case_3()
    print('All test cases passed!')