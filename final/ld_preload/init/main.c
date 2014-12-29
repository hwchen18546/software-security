#include <stdio.h>

void doit()
{
    char input[100];
    printf("Input some string: ");
    gets(input);
    printf("Bye!\n");
}

int main(int argc, char **argv)
{
    doit();
    return 0;
}
