import math
class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    def insertNode(self):
        current = self.head

        while current.next:
            newNodeData = math.gcd(current.data, current.next.data)
            newNode = Node(newNodeData)
            
            temp = current.next
            current.next = newNode
            newNode.next = temp

            current = temp

    def display(self, linkedList):
        current = linkedList
        while current:
            print(current.data)
            current=current.next

# creating linked list
ll = LinkedList()

# creating nodes
node1 = Node(4)
node2 = Node(12)
node3 = Node(12)

# joining nodes
ll.head = node1
node1.next = node2
node2.next = node3

# display nodes's value
ll.display(ll.head)
ll.insertNode()
ll.display(ll.head)
