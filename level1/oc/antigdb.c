#include <stdio.h>
#include <sys/ptrace.h>
int main()
{
    if (ptrace(PTRACE_TRACEME, 0, 1, 0) < 0)
    {
        printf("DEBUGGING...\n");
        return 1;
    }
    printf("Hello\n");
    return 0;
}
