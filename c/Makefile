.PHONY: all
all:
	gcc -O2 -fPIC -Wall -c -o say.o say.c
	gcc -shared say.o -o libsay.so 

.PHONY: run
run:
	python test_say.py

.PHONY: clean
clean:
	rm -f *.o *.so
