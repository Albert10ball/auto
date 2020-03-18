# -*- coding: utf-8 -*-：
# -*-coding:gbk-*

def print_two(*args):
    arg1, arg2 = args
    print "arg1:%r, arg2:%r"%(arg1, arg2)
def print_one(args):
    arg1 = args
    print 'arg1:%r'%arg1

print_one("asdaf")
print_two("dsadsd", "safafs")