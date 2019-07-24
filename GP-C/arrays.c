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

    if (arr->capacity <= arr->count)
    {

        fprintf(stderr, "Yo, INDEXERRORRRRR!");
        return;
    };

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

#ifndef TESTING
int main(void)
{

    Array *arr = create_array(4);

    //arr_insert(arr, "STRING1", 0);
    arr_append(arr, "STRING1");
    arr_read(arr, 0);

    // printf, fprintf, sprintf
    fprintf(stdout, "yo guys, it toally works now lol: %s\n", arr_read(arr, 0));
    //   arr_insert(arr, "STRING2", 0);
    //   arr_insert(arr, "STRING3", 1);
    //   arr_print(arr);
    //   arr_remove(arr, "STRING3");
    //   arr_print(arr);

    destroy_array(arr);

    return 0;
}
#endif
