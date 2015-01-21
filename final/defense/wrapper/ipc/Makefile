
all: wrapper nonblock_wrapper
	chmod 710 wrapper
	chmod 710 nonblock_wrapper

wrapper: wrapper.o loggerfilter.o base64.o
	gcc wrapper.o loggerfilter.o base64.o -o wrapper -m32 -lpthread

nonblock_wrapper: nonblocking-pipe.o loggerfilter.o base64.o
	gcc nonblocking-pipe.o loggerfilter.o base64.o -o nonblock_wrapper -m32

wrapper.o: wrapper.c
	gcc -c wrapper.c -o wrapper.o -m32

nonblocking-pipe.o: nonblocking-pipe.c
	gcc -c nonblocking-pipe.c -o nonblocking-pipe.o -m32	

loggerfilter.o: loggerfilter.c
	gcc -c loggerfilter.c -o loggerfilter.o -m32

base64.o: base64.c
	gcc -c base64.c -o base64.o -m32

clean:
	rm wrapper wrapper.o nonblock_wrapper nonblocking-pipe.o loggerfilter.o base64.o
