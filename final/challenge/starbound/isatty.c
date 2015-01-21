#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>
#include <unistd.h>

int isatty(int fd)
{
	return 1;
}