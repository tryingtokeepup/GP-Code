class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        pass

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        # in the worse case scenario, the element we are bubbling up will need to make its
        # way all the way to the top of the heap
        while index > 0:
            # get the parent element of this index/child
            parent = (index - 1) // 2
            # check if the element at the index is higher priority than its parent
            if self.storage[index] > self.storage[parent]:
                # update the index to be the new spot that our swapped element now resides in
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]

                index = parent
            else:
                # if the value in the index is not higher priority than its parent, then... it's in the right spot!
                # we don't need to do anymore bubble up! let's just exit the loop
                break

    def _sift_down(self, index):
        pass
