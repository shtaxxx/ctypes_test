#include "say.h"

#ifdef __cplusplus
extern "C"
{
#endif

void* createSay()
{
  return (void*) new Say();
}

void deleteSay(void* p)
{
  delete (Say*) p;
}

int hello(void* p, char* s)
{
  std::string ss = s;
  return ((Say*)p)->hello(ss);
}

#ifdef __cplusplus
}
#endif
