from pipes import *
import pipes
import re

def demoFunc(arg1,arg2):
    try:
        obj = pipes.Template()
        ret = obj.copy(arg1,arg2)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
        pass

with open('/dev/null', 'r'):
    infile = ""
    outfile = "xv#m%HHHxJn"
    demoFunc(infile, outfile)
