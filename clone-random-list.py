# Clone a linked list with next and random pointer | Set 1
class Node:
    '''Structure of linked list node'''

    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None


def print_dlist(root):
    '''Function to print the rabdom linked list'''

    curr = root
    while curr != None:
        if curr.random:
            print('Data =', curr.data, ', Random =', curr.random.data)
        else:
            print('Data =', curr.data)

        curr = curr.next


def clone(root):
    clone_list = Node(root.data)

    clone_list_temp = clone_list
    temp = root.next

    while temp:
        clone_list_temp.next = Node(temp.data)
        clone_list_temp = clone_list_temp.next
        temp = temp.next

    clone_list_temp = clone_list
    temp = root

    while clone_list_temp and temp:
        temp_next = temp.next
        temp.next = clone_list_temp
        clone_list_temp.random = temp

        clone_list_temp = clone_list_temp.next
        temp = temp_next

    clone_list_temp = clone_list
    while clone_list_temp:
        clone_list_temp.random = clone_list_temp.random.random.next
        clone_list_temp = clone_list_temp.next

    return clone_list


original_list = Node(1)
original_list.next = Node(2)
original_list.next.next = Node(3)
original_list.next.next.next = Node(4)
original_list.next.next.next.next = Node(5)

'''Set the random pointers'''

# 1's random points to 3
original_list.random = original_list.next.next

# 2's random points to 1
original_list.next.random = original_list

# 3's random points to 5
original_list.next.next.random = original_list.next.next.next.next

# 4's random points to 5
original_list.next.next.next.random = original_list.next.next.next.next

# 5's random points to 2
original_list.next.next.next.next.random = original_list.next

'''Print the original linked list'''
print('Original list:')
print_dlist(original_list)

# clone the list
print("cloned_list  ")

cloned_list = clone(original_list)
print_dlist(cloned_list)

print("original_list  ")
print_dlist(original_list)
