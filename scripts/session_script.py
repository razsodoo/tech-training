from xmlrpc import client

url = 'https://razsodoo-tech-training-18-academy-20924863.dev.odoo.com'
db = 'razsodoo-tech-training-18-academy-20924863'
username = 'admin'
password = 'admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))
model_access = models.execute_kw(db, uid, password, 'academy.session', 'check_access_rights', ['write'], {'raise_exception': False})
print(model_access)

courses = models.execute_kw(db, uid, password, 'academy.course', 'search_read', [[['level', 'in', ['intermidiate','beginner']]]])
print(courses)

course = models.execute_kw(db, uid, password, 'academy.course', 'search', [[['name', 'ilike', 'python']]])
print(course)

session_fields = models.execute_kw(db, uid, password, 'academy.session', 'fields_get', [], {'attributes': ['string', 'type', 'required']})
print(session_fields)

from datetime import datetime, timedelta

# Definimos el start date
date_start = datetime(2025, 6, 5, 10, 0, 0)  # YYYY, MM, DD, HH, MM, SS
# Calculamos el end date (por ejemplo sumando 5 días)
date_end = date_start + timedelta(days=5)

new_session = models.execute_kw(db, uid, password, 'academy.session', 'create', 
                                [{
                                    'course_id': course[0],
                                    'date_start': date_start.strftime('%Y-%m-%d %H:%M:%S'),
                                    'date_end': date_end.strftime('%Y-%m-%d %H:%M:%S')
                                }])

print(new_session)