#include <stdio.h>

int main(void)
{

    // x is type int, unitialized so it has a garbage value

    int x;

    // now x has 12 in it

    x = 12;
    printf("Hey look at x: %d \n", x);

    // Now p has the address of x in it
    // p holds the memory address of x, or otherwise stated, p holds the meory address of where x is in memory
    int *p;
    p = &x;

    printf("This is the address that p is pointing to: %p \n", p);
    printf("I want the actual value of p: %d \n", *p);

    // declaring a pointer
    char *c = "Morning, cool people!";
    // print the actual memory address
    printf("Address of c pointer: %p\n", c);
    // dereferencing the pointer and printing the value
    printf("Value stored at c pointer: %c\n", *c);

    for (int i = 0; i < 22; i++)
    {
        printf("Address: %p | Value: %c\n", c + i, *(c + i));
    }
    return 0;
}