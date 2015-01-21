
all: hook.so isatty.so
	chmod 750 hook.so
	chmod 750 isatty.so
	chmod 750 environment.py

isatty.so: isatty.c
	gcc isatty.c -o isatty.so -fPIC -shared -ldl -D_GNU_SOURCE

hook.so: hook.c
	gcc hook.c -o hook.so -m32 -fPIC -shared -ldl -D_GNU_SOURCE

clean:
	rm isatty.so hook.so
