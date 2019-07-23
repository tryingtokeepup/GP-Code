#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

typedef struct Array
{
    int capacity;    // How many elements can this array hold?
    int count;       // How many states does the array currently hold?
    char **elements; // The string elements contained in the array
} Array;

Array *create_array(int capacity)
{
    // allocate memory for the Array struct
    Array *arr = malloc(sizeof(Array));

    // set initial values for capacity and count
    arr->capacity = capacity;
    arr->count = 0;

    // Allocate memory for elements
    arr->elements = malloc(capacity * sizeof(char *));

    return arr;
}

void destory_array(Array *arr)
{

    // free all the elements
    // loop over all the ... array elements? maybe use count = > i++ till arr->count
    // free(arr->elements[i]

    //free the pointer to the elements (arr->elements)
    //free the actual array
}
int main(void)
{
    Array *arr = create_array(4);

    // Note: adding things to the array like this (this is hard-coded) is for DEMO purpose ONLY.

    arr->elements[0] = "String1";
    arr->elements[1] = "String2";
    return 0;
}