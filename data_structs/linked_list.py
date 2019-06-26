# Implement a Linked List


class Node:
    def __init__(self, value=None, next_node=None):

        # the value at this linked list node
        self.value = value
        # ref to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None
        # reference to the tail of the list
        self.tail = None

    def add_to_tail(self, value):
        # wrap the input value in a node
        # you could leave it blank, but for readability, i added it in
        new_node = Node(value, None)
        # check if there is no head(i.e. the list is actually empty, lol)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        # we have a non-empty list, and so therefore = add the new node to the tail
        else:
            # set the current tail's next ref to our new node
            self.tail.set_next(new_node)
            # set the list's tail ref to the new node
            self.tail = new_node
    # add to the head

    def add_to_head(self, value):
        pass

    def remove_head(self):
        # check if there is no head(i.e. the list is actually empty, lol)
        if not self.head:
            return None
        # if head has no next, then we have a single element in our list
        if not self.head.get_next():
            # get a ref to the head => make a copy of this so we can actually return it later on
            head = self.head
            # delete the list's head's reference, also get rid of the tail's ref
            self.head = None
            self.tail = None
            # return the value, so we know what we just deleted
            return head.get_value()
        value = self.head.get_value()
        # set the head ref to the current head's next node in the list
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        pass

    def contains(self, value):
        if not self.head:
            return False

        # get a ref to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node/ the node that contains the value

        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True

            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten to NULL, or something like this, then the target node isn't in our list
        return False
