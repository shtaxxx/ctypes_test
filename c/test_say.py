import os
import sys
import ctypes 
PATH=os.path.dirname(os.path.abspath(__file__))
NAME='libsay.so'

class Say(object):
    c_say_module = ctypes.CDLL(''.join( (PATH, '/', NAME) ))
    c_say_hello_func_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)
    c_say_hello_func = ctypes.cast(c_say_module.hello, c_say_hello_func_type)
    
    def hello(self, s):
        if s == None or not isinstance(s, str):
            raise TypeError('argument must be str')
        ret = self.c_say_hello_func( ctypes.create_string_buffer(s) )
        print('return : %d' % ret)

if __name__ == '__main__':
    say = Say()
    say.hello("A")
    say.hello("BB")
    say.hello("CCC")
