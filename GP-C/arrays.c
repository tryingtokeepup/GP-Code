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

void resize_array(Array *arr)
{

    int new_capacity = arr->capacity * 2;
    char **new_elements = malloc(new_capacity * sizeof(char *));

    for (int i = 0; i < arr->count; i++)
    {

        new_elements[i] = arr->elements[i];
    }

    // free old element array
    free(arr->elements); // we don't free the individual elements because we still need access to them
    // the new->elements[i] is the same pointer as arr->elements[i]
    arr->elements = new_elements;
    arr->capacity = new_capacity;
}

void destroy_array(Array *arr)
{

    // Free all elements
    for (int i = 0; i < arr->count; i++)
    {
        free(arr->elements[i]);
    }

    // Free array
    free(arr->elements);
    free(arr);
}

void arr_append(Array *arr, char *element)
{

    if (arr->capacity == arr->count)
    {
        resize_array(arr);
    }

    // otherwise, let's copy elements and append to the back of the array
    // strdup is recommended => hidden malloc inside here
    char *element_copy = strdup(element);
    arr->elements[arr->count] = element_copy;

    arr->count++;
}
char *arr_read(Array *arr, int index)
{

    // Throw an error if the index is greater or equal to than the current count
    // you can hit the null character, no biggie, because you disregard it anyway?
    if (index > arr->count)
    {
        //printf("the index is out of range, check it real quick.\n");
        return NULL;
    }
    // Otherwise, return the element at the given index
    //fprintf("Here's the darn thing: %s\n", arr->elements[index]);
    return arr->elements[index];
}

void arr_insert(Array *arr, char *element, int index)
{

    if (index > arr->count)
    {
        // modify this to call the resize function once we write it up!
        fprintf(stderr, "IndexError: Index %d out of range! \n", index);
        return;
    }

    // resize array if number of elements is over capacity
    if (arr->capacity <= arr->count)
    {

        resize_array(arr);
    }
    // move every element after the insert index to the right (by one position)
    for (int i = arr->count; i > index; i--)
    {
        arr->elements[i] = arr->elements[i - 1];
    }
    // copy the element over and add to array (use strdup)
    char *new_element = strdup(element);
    arr->elements[index] = new_element;
    arr->count++;
}

void arr_remove(Array *arr, char *element)
{
    int removed = 0;
    for (int i = 0; i < arr->count; i++)
    {
        if (removed)
        {
            arr->elements[i - 1] = arr->elements[i];
        }
        else if (strcmp(element, arr->elements[i]) == 0)
        {
            free(arr->elements[i]);
            removed = 1;
        }
    }
    if (removed)
    {

        arr->count--;
    }
    else
    {
        fprintf(stderr, "ValueError: %s is not in the array\n", element);
    }
}
/*****
 * Utility function to print an array.
 *****/
void arr_print(Array *arr)
{
    printf("[");
    for (int i = 0; i < arr->count; i++)
    {
        printf("%s", arr->elements[i]);
        if (i != arr->count - 1)
        {
            printf(",");
        }
    }
    printf("]\n");
}

#ifndef TESTING
int main(void)
{

    Array *arr = create_array(1);

    arr_insert(arr, "STRING1", 0);
    arr_append(arr, "STRING4");
    arr_print(arr);

    arr_insert(arr, "STRING2", 0);
    arr_insert(arr, "STRING3", 1);
    arr_print(arr);

    arr_remove(arr, "STRING3");
    arr_print(arr);
    destroy_array(arr);

    return 0;
}
#endif

// int main(void)
// {

//     Array *arr = create_array(4);

//     //arr_insert(arr, "STRING1", 0);
//     arr_append(arr, "STRING1");
//     arr_read(arr, 0);

//     // printf, fprintf, sprintf
//     fprintf(stdout, "yo guys, it toally works now lol: %s\n", arr_read(arr, 0));
//     //   arr_insert(arr, "STRING2", 0);
//     //   arr_insert(arr, "STRING3", 1);
//     //   arr_print(arr);
//     //   arr_remove(arr, "STRING3");
//     //   arr_print(arr);

//     destroy_array(arr);

//     return 0;
// }
