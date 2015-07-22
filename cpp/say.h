#ifndef SAY_H
#define SAY_H

#include <iostream>
#include <string>

class Say
{
private:
  unsigned int num_chars;
public:
  Say();
  int hello(std::string s);
};

#endif
