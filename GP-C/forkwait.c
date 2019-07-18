#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h> // `waitpid` needs to be included separately
#include <string.h>

int main(void)
{

    pid_t pid = fork();

    if (pid == 0)
    {

        printf("Child! \n");
        exit(3);
    }
    else
    {

        printf("Parent! \n");
        // Terminal line dicipline, what the heck is that I need to Google.
        printf("Press return to wait, ignore kai's dumb talk. \n");
        getchar();

        wait(NULL);
        printf("Press Return to exit \n");
        getchar();
    }

    return 0;
}