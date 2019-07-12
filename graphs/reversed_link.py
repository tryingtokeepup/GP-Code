'''
Find Kth element from the end in a singly linked list

1  2  3  4  5  6
A->B->C->D->E->F,
6  5  4  3  2  1

K=4 
D
'''
# Reverse the linked list?
# Let's try using two pointers, fast pointer and a slow pointer
# let's move fast pointer up by ... head.next.next => E (6-4) == 2
# slow pointer is head.next => C


# int our_current_count = 1
# we move from the end node (head)to the next node
# head.next // our_current_count +=1
# while our_current_count < k
# keep moving to the next node
# once we are done with the above, let's ... return the kth node


# def kth_node_from_end(head, k):

#     if head == None:
#         return ("Gosh, please put in an actual linked_list")
#         return -1
#     first_pointer = self.head
#     second_pointer = self.head

#     counter = 1

#     while counter < K:
#         first_pointer.next()
#         # if the above hits a NULL before the counter reaches K, then let's get out of here and return a NULL!
#         if first_pointer == None:
#             return -1 / None
#         else:

#             counter += 1
#     while self.first_pointer.next() != None:

#         self.first_pointer.next()
#         self.second_pointer.next()

#     return second_pointer
