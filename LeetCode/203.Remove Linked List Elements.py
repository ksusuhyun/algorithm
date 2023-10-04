#leetcode 203.Remove Linked List Elements
#leetcode 에서는 removeElements() 함수만 필요함

listA = list(map(int,input().split()))
num = int(input())

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
	
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,x):
        new_Node = Node(x)
        if not self.head:
            self.head = new_Node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_Node

linkedlistA = LinkedList()
for ele in listA:
    linkedlistA.append(ele)

def removeElements(head):
    if head is None:
        return head
    crnt, prev = head, None
    while crnt:
        if crnt.val == num :
            if prev is None:
                head = head.next
                crnt = crnt.next
            else :
                prev.next = crnt.next
                crnt = crnt.next
        else:
            prev = crnt
            crnt = crnt.next
    return head

pri = removeElements(linkedlistA.head) 
if pri == None:
    print("null")
else:
    while pri:
	    print(pri.val, end=' ')
	    pri = pri.next


