#define _GNU_SOURCE
#include <stdio.h>
#include <sys/mman.h>

void patch()
{
    /* 
     * Patch to call a new function.
     * Don't worry about no spaces
     */
    printf("patch is cool~~\n");
}

__attribute__ ((constructor)) void init(void)
{
    printf("Hook init.\n");
    if(mprotect(0x08048000, 0x1000, PROT_WRITE|PROT_READ|PROT_EXEC) == -1)
    {
        printf("mprotect fail\n");
    }
    else
    {
        printf("mark code -rwx\n");
    }
    
    printf("write \"mov eax, &patch; call eax;\" to text-doit()\n");
    /* mov eax, &patch */
    char *ptr_op = 0x804849d; // doit
    *ptr_op = 0xb8; // mov eax
    int *ptr_arg = 0x804849e; //doit + 1
    *ptr_arg = &patch;
    ptr_op = 0x80484a2; // doit + 4
    *ptr_op = 0xff; // call eax
    *(ptr_op + 1) = 0xe0;

    if(mprotect(0x08048000, 0x1000, PROT_WRITE|PROT_READ|PROT_EXEC) == -1)
    {
        printf("mprotect fail\n");
    }
    else
    {
        printf("mark code -r-x\n");
    }

}

