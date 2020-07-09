class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    # utility function to print elements
    def print_list(self):
        arr = []
        if not self.head:
            return arr

        current = self.head

        while current:
            if current.get_next() == None:
                arr.append(current.get_value())
                return arr

            else:
                arr.append(current.get_value())
                current = current.get_next()

        return arr

        

    def reverse_list(self, node, prev):
        # intialize a variable to capture the previous node
        prev = None
        # intialize a variable to capture the current node
        current = self.head 
        while current is not None: 
            # initialize a variable to capture the next node
            next_node = current.get_next()
            # reversing starts here
            # set the current next node to the previous node
            current.set_next(prev)
            # the previous node becomes the current node
            prev = current
            # head becomes previous node 
            self.head = prev 
            # the current node becomes the next node
            current = next_node
        
        # print(self.print_list())




test_list = LinkedList() 
test_list.add_to_head(1)
test_list.add_to_head(2)
test_list.add_to_head(3)
test_list.add_to_head(4)
test_list.add_to_head(5)
test_list.add_to_head(6)

print(test_list.head.value)
print(test_list.print_list())

print(test_list.reverse_list(None, None))
print(test_list.head.value)
