from xmlrpc.client import *
import xmlrpc
import gzip
import http.client
import xmlrpc.client
from io import BytesIO


def demoFunc(arg1,arg2,arg3,arg4):
    try:
        obj = xmlrpc.client.Transport()
        ret = obj.request(arg1,arg2,arg3,arg4)
        repr(obj)
    except (AssertionError, AttributeError, Exception, ImportError, KeyError, LookupError, NotImplementedError, OSError, OverflowError, TypeError, ValueError, gzip.BadGzipFile, http.client.BadStatusLine, http.client.CannotSendHeader, http.client.CannotSendRequest, http.client.HTTPException, http.client.ImproperConnectionState, http.client.IncompleteRead, http.client.InvalidURL, http.client.LineTooLong, http.client.NotConnected, http.client.RemoteDisconnected, http.client.ResponseNotReady, http.client.UnimplementedFileMode, http.client.UnknownProtocol, http.client.UnknownTransferEncoding, xmlrpc.client.Error, xmlrpc.client.Fault, xmlrpc.client.ProtocolError, xmlrpc.client.ResponseError) as e:
        pass


host = "b^wAq18iFelqf!@6"
handler = "02!E&91$VaeI4R2nC6UBJiyb"
request_body = b"b'izCSL'%&$\x00\x00%True"
verbose = True
demoFunc(host, handler, request_body, verbose)
