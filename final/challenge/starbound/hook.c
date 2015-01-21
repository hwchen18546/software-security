#include <stdio.h>
#include <dlfcn.h>
#include <unistd.h>
#include <strings.h>
#include <sys/mman.h>

int puts(const char *s)
{
	int (*old_puts)(const char *s);
	int *fd;

	old_puts = dlsym(RTLD_NEXT, "puts");

	if( strstr(s, "[Info] Portal disabled") )
	{
		fd = 0x080580c4;
		*fd = -1;
	}

	return old_puts(s);
}

void filter_fmt(int fd, char* fmt)
{
	int i;
	for(i = 0; i < strlen(fmt); i++)
	{
		if (fmt[i] == '%')
		{
			if( (i < strlen(fmt) - 1 && fmt[i + 1] != '%'))
			{
				fmt[i] = ' ';
			}
			else
			{
				i++;
			}
		}
	}
	printf(fmt);
}

__attribute__((constructor)) void init(void) 
{
	char *ptr_op;
	int *ptr_arg;

	mprotect(0x8049000, 0x1000, PROT_WRITE|PROT_READ|PROT_EXEC);

	ptr_op = 0x8049cdb;
	ptr_arg = 0x8049cdc;

	*ptr_arg = *ptr_arg + (&filter_fmt - 0x80489F0);   // 0x80489F0 is the position of plt __printf_chk


	mprotect(0x8049000, 0x1000, PROT_READ|PROT_EXEC);
}