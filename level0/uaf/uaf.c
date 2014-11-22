#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
 
typedef struct uaf{
        int n;
        char *buf;
        struct uaf *next;
} Uaf;
 
 
char flag[32];
Uaf *head = NULL;
int count = 0;
 
void add()
{
        char buf[8] = {0};
        unsigned int n;
        printf("uaf to N: ");
        fflush(stdout);
        read(0, buf, sizeof(buf)-1);
        n = atoi(buf);
 
        Uaf *new;
        new = (Uaf*) malloc(sizeof(Uaf));
        new->n = n;
        new->buf = (char*) malloc(10);
        printf("msg: ");
        fflush(stdout);
        read(0, new->buf, 9);
        new->buf[9] = '\0';
        head = new;
}
 
void note()
{
        char buf[8] = {0};
        unsigned int n;
        printf("length: ");
        fflush(stdout);
        read(0, buf, sizeof(buf)-1);
        n = atoi(buf);
 
        char *msg = (char*) malloc(n);
        read(0, msg, n-1);
        printf("%s\n", msg);
        fflush(stdout);
}
 
void nextline()
{
        Uaf *iter = head;
        while (iter){
                if (iter->n < 0){
                        iter = iter->next;
                        continue;
                } else if (iter->n == 0){
                        printf("%s\n", iter->buf);
                        fflush(stdout);
                        free(iter);
                }
                iter->n--;
                iter = iter->next;
        }
}
 
void interact()
{
        char cmd[8] = {0};
 
        write(1, "$ ", 2);
 
        read(0, cmd, sizeof(cmd)-1);
 
        if (!strncmp(cmd, "add", 3)) {
                add();
        } else if (!strncmp(cmd, "\n", 1)) {
                // ignore
        } else if (!strncmp(cmd, "note", 4)) {
                note();
        } else if (!strncmp(cmd, "exit", 4)) {
                exit(0);
        }
 
        nextline();
}
 
 
int main()
{
        FILE *fp = fopen("/home/uaf/flag", "r");
        fscanf(fp, "%s", flag);
        fclose(fp);
 
        char cmd[100];
 
        while (1)
                interact();
}

