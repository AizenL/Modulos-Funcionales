import functools
import xmlrpclib
HOST = '172.17.0.3'
PORT = 8069
DB = 'openacademy'
USER = 'ogm@soluciones4g.com'
PASS = '123456789'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
print "Logged in as %s (uid:%d)" % (USER,uid)
