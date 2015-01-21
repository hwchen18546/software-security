#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
#include <fcntl.h>
#include <time.h>
#include "loggerfilter.h"
#define BUFFSIZE 1024
#define PARENT_READ pipefd2[0]
#define PARENT_WRITE pipefd[1]
#define CHILD_READ pipefd[0]
#define CHILD_WRITE pipefd2[1]

void bye()
{
    exit(0);
}

int main(int argc, char * argv[])
{
    pid_t pid;
    int n;
    int pipefd[2], pipefd2[2], pipefd3[3];
    char buf[BUFFSIZE];

    init(0);

    pipe(pipefd);
    pipe(pipefd2);
    pipe(pipefd3);
    pid = fork();
    if(pid == 0) // client
    {
        close(PARENT_READ);
        close(PARENT_WRITE);
        dup2(CHILD_READ, 0);
        dup2(CHILD_WRITE, 1);
        runTargetProgram();
    }
    else // parent
    {
        // when child died
        signal(SIGCHLD, bye);
        close(2);
        close(CHILD_READ);
        close(CHILD_WRITE);
        if(fcntl(0, F_SETFL, O_NONBLOCK) == -1
                || fcntl(PARENT_READ, F_SETFL, O_NONBLOCK) == -1) 
        {   
            //fprintf(stderr, "Call to fcntl failed.\n");
            exit(1);
        }
        while(1)
        {
            // hijack input
            bzero(buf, BUFFSIZE);
            n = read(0, buf, BUFFSIZE);
            if(n == -1 && errno == EAGAIN)
            {   
                if(errno == EAGAIN)
                {   
                    // no input
                }   
                else
                {   
                    //fprintf(stderr, "read stdin failed.\n");
                }   
            }   
            else if(n == 0)
            {   
                //fprintf(stderr, "stdin close.\n");
            }   
            else
            {   
                logInput(buf, n);
                inputFilter(buf, n);
                //logger(buf , 2);
                write(PARENT_WRITE, buf, n);
            } 

            // hijack output
            bzero(buf, BUFFSIZE);
            n = read(PARENT_READ, buf, BUFFSIZE);
            if(n == -1 && errno == EAGAIN)
            {   
                if(errno == EAGAIN)
                {   
                    // no input
                }   
                else
                {   
                    //fprintf(stderr, "read pipe failed.\n");
                }   
            }   
            else if(n == 0)
            {   
                //fprintf(stderr, "pipe close.\n");
            }   
            else
            {   
                logOutput(buf, n);
                outputFilter(buf, n);
                write(1, buf, n);
            } 
        }
    }
    return 0;
}
