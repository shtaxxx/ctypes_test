#include <stdio.h>

static unsigned int num_chars = 0;

int hello(char *s){
  num_chars += printf("Hello, %s\n", s);
  return num_chars;
}

