.PHONY: all
all:
	g++ -O2 -fPIC -Wall -c -o say.o say.cc 
	g++ -O2 -fPIC -Wall -c -o say_wrapper.o say_wrapper.cc 
	g++ -shared say_wrapper.o say.o -o libsay.so 

.PHONY: run
run:
	python test_say.py

.PHONY: clean
clean:
	rm -f *.o *.so
