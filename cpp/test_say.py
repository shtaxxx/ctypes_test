import os
import sys
import ctypes 
PATH=os.path.dirname(os.path.abspath(__file__))
NAME='libsay.so'

class Say(object):
    so = ctypes.CDLL(''.join( (PATH, '/', NAME) ))

    def __init__(self):
        self.so.createSay.restype = ctypes.c_void_p
        self.say = self.so.createSay()

    def __del__(self):
        self.so.deleteSay.argtypes = [ctypes.c_void_p]
        self.so.deleteSay(self.say)

    def hello(self, s):
        if s == None or not isinstance(s, str):
            raise TypeError('argument must be str')
        self.so.hello.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        self.so.hello.restypes = [ctypes.c_int]
        ret = self.so.hello( self.say, ctypes.create_string_buffer(s) )
        print('return : %d' % ret)

if __name__ == '__main__':
    say = Say()
    say.hello("A")
    say.hello("BB")
    say.hello("CCC")
