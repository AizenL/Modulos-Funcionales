import functools
import xmlrpclib
<<<<<<< HEAD
HOST = '172.17.0.3'
=======
HOST = '172.17.0.2'
>>>>>>> 9a0fa86595516bd0be322d5373e1b1474654748c
PORT = 8069
DB = 'openacademy'
USER = 'ogm@soluciones4g.com'
PASS = '123456789'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
print "Logged in as %s (uid:%d)" % (USER,uid)
<<<<<<< HEAD
=======

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


# 3.create a new session
method_name = 'create'

responsible_id = call('res.partner', 'search', [('name', '=', 'OGGonzalezM')])[0]
print "Responsible id ", responsible_id

method_name = 'create'
course_id = call('openacademy.course', method_name, {'name': 'Getting upper ne', 'responsible_id':3})

model = 'openacademy.session'
session_id = call(model, method_name, {
    'name' : 'From WS',
    'instructor_id': responsible_id,
    'course_id' : course_id,
    'attendee_ids': [(4, 39), (4, 38)]
})
print "New session id ", session_id
>>>>>>> 9a0fa86595516bd0be322d5373e1b1474654748c
