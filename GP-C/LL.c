#include <stdlib.h>
#include <stdio.h>

typedef struct Node
{

    struct Node *next;
    int value;
} Node; // I think this gives you a quick shortcut to the name parameter Node

typedef struct LinkedList
{

    Node *head;
    Node *tail;
    int size;
} LinkedList;

LinkedList *create_list(void)
{

    LinkedList *ll = malloc(sizeof(LinkedList));
    ll->head = NULL;
    ll->tail = NULL;
    ll->size = 0;

    return ll;
}

void free_list(LinkedList *ll)
{

    if (ll)
    {

        free(ll);
    }
}

Node *create_node(int value, Node *next)
{

    Node *node = malloc(sizeof(Node));
    node->value = value;
    node->next = next;

    return node;
}

void free_node(Node *node)
{
    if (node)
    {

        free(node);
    }
}

// inserts at the tail of the list
void list_insert(LinkedList *ll, int value)
{

    // since we're adding to the the tail
    // this node won't have a next node at this point
    Node *new_node = create_node(value, NULL);
    // make sure we set the last node in the list's
    // next value first before updating the list's tail pointer

    if (ll->head == NULL)
    {

        ll->head = new_node;
    }

    if (ll->tail == NULL)
    {
        ll->tail = new_node;
    }
    else
    {

        ll->tail->next = new_node; // appending the node to the end of the list, which is tail->next
    }
    // now we can set the tail pointer of the list after we've set the old tail's next pointer
    // to point to the new node

    ll->tail = new_node;
    ll->size++;
}

// Returns the target item if it is in the list, Returns -1 if it doesn't exist in the list

int list_search(LinkedList *ll, int target)
{

    // current node pointer keeps track of where we are in the list as we're iterating
    Node *current = ll->head;
    // so long as current is valid, keep iterating

    while (current)
    {

        // check if the value of the current node matches th target value we're looking for
        if (current->value == target)
        {

            // if so, return it
            return current->value;
        }
        //otherwise, move on to the next node by setting current to the next node in the list
        current = current->next;
    }
    // at this point, we've reached the end of the list and haven't found the node; return -1
    return -1;
}

// Deletes a node if it contains the target value
// Returns -1 if no such node exists in the list
int list_delete(LinkedList *ll, int target)
{
    // boolean indicating if we've found the target
    int found = 0;
    // previous node pointer that keeps track of the
    // list node behind the current node we're
    // iterating on; this is necessary because we're
    // walking through a singly-linked list and
    // cannot backtrack
    Node *previous = NULL;
    // current node we're iterating on in the list
    Node *current = ll->head;
    // keep iterating so long as current points to a
    // valid node and `found` is not a truthy value
    while (current && !found)
    {
        if (current->value == target)
        {
            found = 1;
        }
        else
        {
            // if the current node doesn't contain the value
            // we're looking for, set `previous` to the `current`
            // node and set `current` to the next node in the list
            previous = current;
            current = current->next;
        }
    }
    // at this point we've reached the end of the list
    // if current is NULL here then that means we've traversed the
    // entire list and none of them matched the target we were
    // looking for, so return -1
    if (current == NULL)
    {
        return -1;
    }
    // if `previous` is NULL, then that means that we stopped iterating
    // immediately, meaning that the head of the list contained the value
    // we were looking for, so we want to remove the head node of the list
    // to do this, we move the head pointer to the next node in the list
    // and free the old head node
    if (previous == NULL)
    {
        // get a reference to the node we're going to delete so that
        // we still have a reference for us to free
        Node *node_to_delete = ll->head;
        ll->head = current->next;
        free_node(node_to_delete);
    }
    // otherwise, we found a node whose value matches the target we're
    // looking for, so now we want to remove it from the list
    // we do this by setting the previous node to the current node's (the
    // one that we're removing) next node, so that the current node
    // has no pointers pointing to it
    // then we free the current node
    else
    {
        // get a reference to the node we're going to delete so that
        // we still have a reference for us to free
        Node *node_to_delete = current;
        // setting the previous node's next to be the current node's
        // next skips over the current node in the list
        previous->next = current->next;
        free_node(node_to_delete);
    }
    ll->size--;

    return 0;
}

int main(void)
{

    LinkedList *ll = create_list();
    list_insert(ll, 1);
    list_insert(ll, 2);
    list_insert(ll, 3);
    printf("Should print 2: %d\n", list_search(ll, 2));
    list_delete(ll, 2);
    printf("Should print -1: %d\n", list_search(ll, 2));
    free_list(ll);

    return 0;
}