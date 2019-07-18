#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <string.h>
#define PROMPT "Type something in please. \n"
int main(void)
{

    char commandline[8192];

    while (1)
    {
        printf(">>$ ");
        fflush(stdout);
        // print out a prompt, so the user knows that he/she needs to type something in
        printf("%s", PROMPT);
        fgets(commandline, sizeof(commandline), stdin);
        // printf("user passed in: %s\n", commandline);
        // Strip newline off the end
        printf("command looks like this: '%s'\n", commandline);
        commandline[strlen(commandline) - 1] = '\0';

        // Check for exit built-in command to exit shell
        if (strcmp(commandline, "exit") == 0)
        {

            break;
        }
        pid_t pid = fork();

        if (pid == 0)
        {
            // This is odd, let's see what this turns into.
            execlp(commandline, commandline, NULL);
            perror("exec");
            exit(1);
        }
        else
        {

            wait(NULL);
        }
    }

    return 0;
}
