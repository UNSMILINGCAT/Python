import os
import sqlite3

connect = sqlite3.connect('sample_database')
cursor = connect.cursor()
# create tables
cursor.execute("""
create table employee(empid integer,firstname varchar,lastname varchar,
dept integer,manager integer,phone varchar)""")
cursor.execute("""
create table department (departmentid integer,name varchar, manager integer)""")
cursor.execute("""
create table user(userid integer,username varchar,employeeid integer)""")
# create indices
cursor.execute("""create index userid on user(userid)""")
cursor.execute("""create index empid on employee(empid)""")
cursor.execute("""create index deptid on department (departmentid)""")
cursor.execute("""create index deptfk on employee(dept)""")
cursor.execute("""create index mgr on employee(manager)""")
cursor.execute("""create index emplid on user(employeeid)""")
cursor.execute("""create index deptmgr on department(manager)""")
connect.commit()
cursor.close()
connect.close()
