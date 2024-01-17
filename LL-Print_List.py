class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        pointer = self.head
        while pointer is not None:
            print(pointer.value)
            pointer = pointer.next
        
        
    def append(self, value):
        last_node = Node(value)
        if self.head is None:
            self.head = last_node
            self.tail = last_node
        else:
            self.tail.next = last_node
            self.tail = last_node
        self.length += 1
        return True

my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

my_linked_list.print_list()


# Output:
# 11
# 3
# 23
# 7
