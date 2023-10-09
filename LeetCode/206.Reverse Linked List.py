#leetcode 206.Reverse Linked List
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def createList(in_list: List[int]) -> ListNode:
    if len(in_list) == 0:
        raise RuntimeError("in_list must have data")
    head_node = ListNode(in_list[0])
    last_node = head_node
    for idx in range(1, len(in_list)):
        node = ListNode(in_list[idx])
        last_node.next = node
        last_node = node
    return head_node


def printNodes(node: ListNode):
    crnt_node = node
    while crnt_node is not None:
        print(crnt_node.val, end=' ')
        crnt_node = crnt_node.next
    print()


class ReverseList:
    def iterativeWay(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        elif head.next is None:
            return head

        crnt_node = head.next
        prev_node = head
        head.next = None

        while crnt_node:
            tmp_next_node = crnt_node.next
            crnt_node.next = prev_node
            prev_node = crnt_node
            crnt_node = tmp_next_node

        return prev_node

    def recursiveWay(self, head: ListNode) -> ListNode:
        # exit condition
        if head is None:
            return head
        elif head.next is None:
            return head

        back_head = self.recursiveWay(head.next)
        head.next.next = head
        head.next = None

        return back_head