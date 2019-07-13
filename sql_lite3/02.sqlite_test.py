import sqlite3

conn = sqlite3.connect('sql_lite3/example.db')
c = conn.cursor()
symbol = 'RHAT'
c.execute("select * from stocks where symbol='%s'"%symbol)
itmes = c.fetchall()

for itme in itmes:
    print(itme)

t = ('RHAT',)
sql = 'select * from stocks where symbol = ?'
c.execute(sql,t)
print(c.fetchall())

c.execute('select * from stocks order by price')
rows = c.fetchall()
for row in rows:
    print(row)

c.close()