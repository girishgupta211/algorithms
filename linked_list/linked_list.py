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


# Code execution starts here
if __name__ == '__main__':
    # node1 = Node(1)
    # print(node1.data)
    # print(node1.next)
    # print(node1)
    #
    # node2 = Node(2)
    # print(node2.data)
    # print(node2.next)
    # print(node2)
    #
    # node1.next = node2
    # print(node1.next.data)
    #
    # node3 = Node(3)
    # print(node3.data)
    # print(node3.next)
    # print(node3)
    #
    # node2.next = node3
    #
    # print(node1.data)
    # print(node1.next.data)
    # print(node1.next.next.data)

    # Start with the empty list
    llist = LinkedList()
    print(llist)
    print(llist.head)
    node1 = Node(1)

    llist.head = node1
    print(llist.head)

    node2 = Node(2)
    node1.next = node2
    print(llist)

    node3 = Node(3)
    node2.next = node3

    # print all element in linked list
    temp = llist.head
    while temp:
        print(temp.data)
        temp = temp.next

    ''' 
    Three nodes have been created. 
    We have references to these three blocks as head, 
    second and third 

    llist.head	 node2			 node3 
        |			 |				 | 
        |			 |				 | 
    +----+------+	 +----+------+	 +----+------+ 
    | 1 | None |	 | 2 | None |	 | 3 | None | 
    +----+------+	 +----+------+	 +----+------+ 
    '''

    ''' 
    Now next of first Node refers to second. So they 
    both are linked. 

    llist.head	 node2			 node3 
        |			 |				 | 
        |			 |				 | 
    +----+------+	 +----+------+	 +----+------+ 
    | 1 | o-------->| 2 | null |	 | 3 | null | 
    +----+------+	 +----+------+	 +----+------+ 
    '''

    ''' 
    Now next of second Node refers to third. So all three 
    nodes are linked. 

    llist.head	 node2			 node3 
        |			 |				 | 
        |			 |				 | 
    +----+------+	 +----+------+	 +----+------+ 
    | 1 | o-------->| 2 | o-------->| 3 | null | 
    +----+------+	 +----+------+	 +----+------+ 
    '''
