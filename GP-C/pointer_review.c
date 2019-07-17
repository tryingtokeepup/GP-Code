#include <stdio.h>

int main(void)
{

    int a[5] = {11, 15, 34, 45, 56};

    for (int i = 0; i < 5; i++)
    {
        printf("Address: %p | Value: %d\n", a + i, *(a + i));
    };
    int *p = &a[2];
    *p = 700;
    *(p + 1) = 1000; // change a[3] to 1000

    printf("arr[2] is NOW changed to: %d \n", a[2]);
    printf("arr[3] is NOW changed to: %d \n", a[3]);

    for (int i = 0; i < 5; i++)
    {
        printf("Address: %p | Value: %d\n", a + i, *(a + i));
    }
    return 0;
}