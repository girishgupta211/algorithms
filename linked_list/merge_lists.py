# A simple Python program to introduce a linked list

# Node class


class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None


def merge_lists(llist1, llist2):
    if llist2.head is None:
        return llist1

    if llist1.head is None:
        return llist2

    merged_list = LinkedList()

    llist1 = llist1.head
    llist2 = llist2.head

    temp = None

    if llist1.data < llist2.data:
        temp = llist1
        llist1 = llist1.next
    else:
        temp = llist2
        llist2 = llist2.next

    merged_list.head = temp

    while llist1 and llist2:
        if llist1.data < llist2.data:
            temp.next = llist1
            llist1 = llist1.next
        else:
            temp.next = llist2
            llist2 = llist2.next
        temp = temp.next

    if llist1:
        temp.next = llist1

    if llist2:
        temp.next = llist2

    return merged_list


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist1 = LinkedList()
    node1 = Node(1)

    llist1.head = node1

    node2 = Node(3)
    node1.next = node2

    node3 = Node(5)
    node2.next = node3

    node4 = Node(7)
    node3.next = node4

    # Start with the empty list
    llist2 = LinkedList()
    node1 = Node(2)

    llist2.head = node1

    node2 = Node(4)
    node1.next = node2

    node3 = Node(6)
    node2.next = node3

    node4 = Node(8)
    node3.next = node4

    node5 = Node(10)
    node4.next = node5

    print(llist1)
    print(llist2)

    result = merge_lists(llist1, llist2)
    temp = result.head
    while temp:
        print(temp.data)
        temp = temp.next
