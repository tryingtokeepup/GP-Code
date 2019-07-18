#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int main(void)
{

    char buffer[128];
    //p[0] will be the read end of the pipe
    //p[1] will be the write end of the pipe

    int pipe_descriptor[2];

    // creat ethe pipe and populate it with integers
    pipe(pipe_descriptor);
    // This is where you'd fork() if you want to do interprocess-communication

    // Send data down the pipe
    int bytes_written = write(pipe_descriptor[1], "Hello World! \n", 14);
    // Error check
    if (bytes_written == -1)
    {
        perror("write");
        exit(1);
    }
    // Read the data from the pipe
    int bytes_read = read(pipe_descriptor[0], buffer, sizeof buffer);

    // Write the data to the screen
    write(STDOUT_FILENO, buffer, bytes_read);

    return 0;
}