# A simple Python program to sort linked list using merge sort

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


def merge_sort(llist):
    if llist is None:
        return llist

    if llist.next is None:
        return llist

    mid = llist
    fast = llist

    while fast and fast.next:
        if fast.next.next is None:
            break

        mid = mid.next
        fast = fast.next.next

    first = llist
    second = mid.next

    mid.next = None

    first = merge_sort(first)
    second = merge_sort(second)

    return merge_lists(first, second)


# 1, 3, 2 , 4 --> 1, 3 --> 1  -> 3 -> merge_lists(1,3)  first(1,3) -->
# 2, 4 --> 2 -> 4 -> merge_lists(2, 4 ) second(2,4) -> merge_lists (1, 3 ) (2,4) -> (1, 2, 3, 4)


def merge_lists(llist1, llist2):
    if llist2 is None:
        return llist1

    if llist1 is None:
        return llist2

    temp = None

    if llist1.data < llist2.data:
        temp = llist1
        llist1 = llist1.next
    else:
        temp = llist2
        llist2 = llist2.next

    merged_list = temp

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

    node5 = Node(2)
    node4.next = node5

    # Start with the empty list
    llist2 = LinkedList()
    node1 = Node(2)

    llist2.head = node1

    node2 = Node(5)
    node1.next = node2

    node3 = Node(3)
    node2.next = node3

    node4 = Node(1)
    node3.next = node4

    print(llist1)
    print(llist2)

    print("Sort 1")
    result = merge_sort(llist2.head)
    temp = result
    while temp:
        print(temp.data)
        temp = temp.next

    print("Sort 2")
    result = merge_sort(llist1.head)
    temp = result
    while temp:
        print(temp.data)
        temp = temp.next
