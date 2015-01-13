#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <time.h>
#define BUFFSIZE 1024
#define PARENT_READ pipefd2[0]
#define PARENT_WRITE pipefd[1]
#define CHILD_READ pipefd[0]
#define CHILD_WRITE pipefd2[1]
#define CHILD_PATH "/home/hwchen18546/secprog/final/wrapper"
#define CHILD_NAME "simpleshell"

void bye()
{
    exit(0);
}

void filter(char *buf)
{
    if(strstr(buf, "flag"))
    {
        exit(0);
    }    
}

int main(int argc, char * argv[])
{
    pid_t pid;
    int n;
    int pipefd[2], pipefd2[2];
    char buf[BUFFSIZE];
    
    pipe(pipefd);
    pipe(pipefd2);
    pid = fork();
    if(pid == 0) // client
    {
        close(PARENT_READ);
        close(PARENT_WRITE);
        dup2(CHILD_READ, 0);
        dup2(CHILD_WRITE, 1);
        chdir(CHILD_PATH);
        execve(CHILD_NAME, NULL, NULL);
    }
    else // parent
    {
        // when child died
        signal(SIGCHLD, bye);

        close(CHILD_READ);
        close(CHILD_WRITE);
        // read first msg from child
        n = read(PARENT_READ, buf, BUFFSIZE);
        write(1, buf, n);
        while(1)
        {
            // hijack input
            bzero(buf, BUFFSIZE);
            n = read(0, buf, BUFFSIZE);
            write(PARENT_WRITE, buf, n);

            // hijack output
            bzero(buf, BUFFSIZE);
            n = read(PARENT_READ, buf, BUFFSIZE);
            filter(buf);
            write(1, buf, n);
        }
    }
    return 0;
}
