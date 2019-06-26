
class Node:
    def __init__(self, value=None, next_node=None, prev_node=None):

        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def getValue(self):
        return self.value

    def get_next(self):
        return self.next_node

    def get_prev(self):
        return self.prev_node

    def set_next(self, new_next):
        self.next_node = new_next

    def set_prev(self, new_prev):
        self.prev_node = new_prev


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.counter = 0
        self.tail = None

    def __str__(self):
        array = []

        def all_nodes_printed(node):
            nonlocal array
            array.append(node.value)
        self.traverse(all_nodes_printed)
        return str(array)

    def add_to_tail(self, new_tail):
        # check if our list is empty
        if self.get_size() == 0:
            new_node = Node(new_tail)
            self.tail = new_node
            self.head = new_node

        elif self.get_size() == 1:
            new_node = Node(new_tail)
            self.head.set_next(new_node)
            new_node.set_prev(self.tail)
            self.tail = new_node

        else:
            new_node = Node(new_tail)
            self.tail.set_next(new_node)
            new_node.set_prev(self.tail)
            self.tail = new_node
        self.increment_counter()

    def add_to_head(self, new_head):
        if self.get_size() == 0:
            new_node = Node(new_head)
            self.tail = new_node
            self.head = new_node

        elif self.get_size() == 1:
            new_node = Node(new_head)
            self.tail.set_prev(new_node)
            new_node.set_next(self.head)
            self.head = new_node

        else:
            new_node = Node(new_head)
            self.head.set_prev(new_node)
            new_node.set_next(self.head)
            self.head = new_node
        self.increment_counter()

    def contains(self, value):
        pass

    def remove_from_head(self):
        pass

    def remove_from_tail(self):
        pass

    def insert_value(self, value):
        pass

    def remove_value(self, value):
        pass

    def increment_counter(self):
        self.counter += 1

    def decrement_counter(self):
        self.counter -= 1

    def get_size(self):
        return self.counter

    def traverse(self, cb):

        temp = self.head

        while temp != None:

            cb(temp)
            temp = temp.get_next()


kai_list = DoubleLinkedList()


# kai_list.add_to_head(5)

# kai_list.add_to_head(4)
kai_list.add_to_tail(18)
kai_list.add_to_tail(5)

print(kai_list)
