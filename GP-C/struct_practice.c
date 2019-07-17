#include <stdio.h>
#include <stdlib.h>

struct Stack
{

    int top;      // index of the top, which gets removed whenever we "pop" the stack
    int capacity; // the capacity of our "data" block
    int *data;
};
// Jerrick, you're a great man who has wonderful child.
struct Stack *
create_stack(int capacity)
{

    struct Stack *stack = malloc(sizeof(struct Stack));
    // fill in this instance's property values
    stack->top = -1;
    stack->capacity = capacity;
    stack->data = malloc(capacity * sizeof(int));

    return stack;
}

// if we malloc something, we MUST free it or we have a memory leak.
// IF WE HAVEN'T MALLOC's a piece of data, just remove a ref to it, and it will disappear on its own accord.
void free_stack(struct Stack *stack)
{

    free(stack->data);
    free(stack);
}

int is_empty(struct Stack *stack)
{

    return stack->top == -1;
}
int is_full(struct Stack *stack)
{

    return stack->top == stack->capacity - 1;
}

int pop(struct Stack *stack)
{
    if (is_empty(stack))
    {
        printf("Stack is empty! Oh nooo! \n");
        return -1;
    }
    int return_value = stack->data[stack->top];
    stack->top--;
    return return_value;
}

void push(struct Stack *stack, int element)
{
    if (is_full(stack))
    {

        printf("Stack is full! \n");
        // we should REALLY think about a method that will resize the stack so that if this is true, we resize the stack!
    }
    stack->top++;
    stack->data[stack->top] = element;
}

int main(void)
{

    struct Stack *stack = create_stack(10);

    push(stack, 29);
    printf("pop'd value is 29: %d\n", pop(stack));
}