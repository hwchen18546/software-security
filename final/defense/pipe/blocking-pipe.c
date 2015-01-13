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
#define CHILD_NAME "test"
#define LOG_PATH "/home/hwchen18546/secprog/final/wrapper"

FILE *log_f;
char log_name[100];

void logger(char *buf, int fun)
{
    time_t rawtime;
    struct tm *timeinfo;
    time(&rawtime);
    timeinfo = localtime(&rawtime);
    switch(fun)
    {
        case 0: //init
            sprintf(log_name, "%s/log-%ld", LOG_PATH, rawtime);
            log_f = fopen(log_name, "w");
            fprintf(log_f, "-- %sStart logger\n\n", asctime(timeinfo));
            fclose(log_f);
            break;
        case 1: //server send
            log_f = fopen(log_name, "a");
            fprintf(log_f, "-- %sServer Send:\n%s\n\n", asctime(timeinfo), buf);
            fclose(log_f);
            break;
        case 2: //client send
            log_f = fopen(log_name, "a");
            fprintf(log_f, "-- %sClient Send:\n%s\n\n", asctime(timeinfo), buf);
            fclose(log_f);
            break;
        case 3: //filter block
            log_f = fopen(log_name, "a");
            fprintf(log_f, "-- %sFilter block:\n%s\n\n", asctime(timeinfo), buf);
            fclose(log_f);
            break;
        case 4: //end
            log_f = fopen(log_name, "a");
            fprintf(log_f, "-- %s%s\n", asctime(timeinfo), buf);
            fclose(log_f);
            break;
    }
}

void bye()
{
    logger("Server close()\n", 4);
    exit(0);
}

void filter(char *buf)
{
    if(strstr(buf, "flag"))
    {
        logger(buf, 3);
        exit(0);
    }    
}

int main(int argc, char * argv[])
{
    pid_t pid;
    int n;
    int pipefd[2], pipefd2[2];
    char buf[BUFFSIZE];
    logger("" , 0);
    
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
        logger(buf , 1);
        while(1)
        {
            // hijack input
            bzero(buf, BUFFSIZE);
            n = read(0, buf, BUFFSIZE);
            logger(buf , 2);
            write(PARENT_WRITE, buf, n);

            // hijack output
            bzero(buf, BUFFSIZE);
            n = read(PARENT_READ, buf, BUFFSIZE);
            logger(buf , 1);
            filter(buf);
            write(1, buf, n);
        }
    }
    return 0;
}
