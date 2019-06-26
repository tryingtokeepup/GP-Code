# we need to make a class
class BinarySearchTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # def __str__(self):
    #     array = []

    #     def all_nodes_printed(node):
    #         nonlocal array
    #         array.append(node.value)
    #     self.traverse(all_nodes_printed)
    #     return str(array)

    def insert(self, value):
        # first thing we need to do, is to wrap the value in a node
        # new_node = BinarySearchTree(value)
        # for this example, we'll instantiate that node later on
        # 1) compare the element/value against the current node value
        # 2) based on the comparison (less/more), we go left or right
        # 3) if empty spot, we park the value/node in there
        # 4) else/otherwise, we ... start from step 1, do it all over again
        # Base Case == Number 3!
        if value < self.value:
            # let's check if there's a value there
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        pass

    # def traverse(self, cb):

    #     temp = self.value

    #     while temp != None:

    #         cb(temp)
    #         temp = temp.left()
    #         temp = temp.right()


root = BinarySearchTree(15)
root.insert(90)
root.insert(4)
print(root.value)
print(root.right.value)
print(root.left.value)
# print(root)
