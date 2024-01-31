import mysql.connector
import webbrowser

conn = mysql.connector.connect(
    user='root',
    password='Root@123',
    host='localhost',
    database='db_python'
)

if conn:
    print ("Connected Successfully")
else:
    print ("Connection Not Established")

select_employee = """SELECT * FROM students"""
cursor = conn.cursor()
cursor.execute(select_employee)
result = cursor.fetchall()

p = []

tbl = "<tr><td>ID</td><td>Matricula</td><td>Nome</td><td>Sobrenome</td></tr>"
p.append(tbl)

for row in result:
    a = "<tr><td>%s</td>"%row[0]
    p.append(a)
    b = "<td>%s</td>"%row[1]
    p.append(b)
    c = "<td>%s</td>"%row[2]
    p.append(c)
    d = "<td>%s</td></tr>"%row[3]
    p.append(d)


contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta content="text/html; charset=UTF-8"
http-equiv="content-type">
<title>Python Web Browser</title>
</head>
<body>
<table>
%s
</table>
</body>
</html>
'''%(p)

filename = '.venv/index.html'

def main(contents, filename):
    output = open(filename,"w")
    output.write(contents)
    output.close()

main(contents, filename)
webbrowser.open(filename)

if(conn.is_connected()):
    cursor.close()
    conn.close()
    print("MySQL connection is closed.")