from operator import *
import operator


def demoFunc(arg1,arg2):
    try:
        ret = operator.lshift(arg1,arg2)
    except (AssertionError, AttributeError, ImportError, LookupError, OSError, TypeError, ValueError) as e:
        pass
    
a= 15877407210
b= 21291076407210
demoFunc(a, b)
