#include "say.h"

Say::Say()
{
  this->num_chars = 0;
}

int Say::hello(std::string s)
{
  std::string p = "Hello, " + s;
  this->num_chars += p.length() + 1; // for endl
  std::cout << p << std::endl;
  return this->num_chars;
}

