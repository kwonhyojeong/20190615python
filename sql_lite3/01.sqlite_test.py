import sqlite3

print(sqlite3.version)

conn = sqlite3.connect('sql_lite3/example.db')

c = conn.cursor()

c.execute('''
            create table if not exists stocks(
                date text,
                trans text,
                symbol text,
                qty real,
                price real
)
''')

c.execute('''
            insert into stocks(date, trans, symbol, qty, price)
                        values('2006-0105','BUY','RHAT',100.2,35.14)
''')

conn.commit()
conn.close