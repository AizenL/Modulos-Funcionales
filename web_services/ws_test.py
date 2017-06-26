import functools
import xmlrpclib
HOST = '172.17.0.2'
PORT = 8069
DB = 'openacademy'
USER = 'ogm@soluciones4g.com'
PASS = '123456789'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
print "Logged in as %s (uid:%d)" % (USER,uid)

call = functools.partial(
    xmlrpclib.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)

model = 'openacademy.session'
domanin = []
method_name = 'search_read'
sessions = call(model, method_name, domanin, ['name', 'seats', 'taken_seats'])
print "Sessions", sessions

for session in sessions:
    print "Session %s (%s seats) Taken Seats %d" % (session['name'], session['seats'], session['taken_seats'])

method_name = 'search'
domanin = [('name', '=', 'Backend Odoo')]
course_ids = call('openacademy.course', method_name, domanin)
print "Course IDs ", course_ids

method_name = 'create'
course_id = call('openacademy.course', method_name, {'name': 'Backend1 Odoo'})

# 3.create a new session
session_id = call('openacademy.session', 'create', {
    'name' : 'My session',
    'course_id' : 1,
})
print "New session id ", session_id 
