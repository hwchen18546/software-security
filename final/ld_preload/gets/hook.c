#define _GNU_SOURCE
#include <dlfcn.h>
#include <stdio.h>
#include <string.h>
#include <time.h>


char *gets(char *str)
{
    /* origin gets */
    char *(*old_gets)(char *msg);
    old_gets = dlsym(RTLD_NEXT, "gets");
    old_gets(str);    
    /* debugging */
    printf("Hook: %s\n", str);
    /* filter */
    char *filter_str = "flag";
    char *ret = strstr(str, filter_str);
    if(ret)
    {
        strncpy(ret, "fuck", 4);
    }
    /* logger */
    char log[100];
    time_t rawtime;
    struct tm *timeinfo;
    time (&rawtime);
    timeinfo = localtime(&rawtime);
    sprintf(log, "--Time: %s  Input: %s\n", asctime(timeinfo), str);
    FILE *f = fopen("log", "a+");
    fwrite(log, strlen(log), 1, f);
    fclose(f);
    return str;
}

