import sqlite3

def create_table():
    conn = sqlite3.connect('sql_lite3/my_books.db')
    c = conn.cursor()
    c.execute('''create table if not exists books(
        title text,
        published_date text,
        publisher text,
        pages integer,
        recommend integer
    )''')

    conn.commit()
    conn.close()

    
def insert_books():
    conn = sqlite3.connect("sql_lite3/my_books.db")
    c = conn.cursor()
    c.execute("insert into books values('Java','2019-05-20','길벗',500,10)")
    sql = 'insert into books values(?,?,?,?,?)'
    c.execute(sql,('Python','201001','한빛',584,20))
    items = [
            ('빅데이터','2014-07-02','삼성',296,11),
            ('안드로이드','2010-02-02','삼성',526,20),
            ('spring','2013-12-02','삼성',248,15)
        ]
    c.executemany(sql,items)
    conn.commit()
    conn.close()



def all_books():
    conn = sqlite3.connect("sql_lite3/my_books.db")
    c = conn.cursor()
    c.execute("select * from books")
    print('[1] 전체 데이터 출력하기')
    books = c.fetchall()
    print(type(books))
    print(len(books))

    for book in books:
        for i in books:
            print(i, end=" ")
        print()

    conn.close()



def some_books(number):
    conn = sqlite3.connect("sql_lite3/my_books.db")
    c = conn.cursor()
    c.execute("select * from books")
    books = c.fetchmany(number)

    for book in books:
        for i in book:
            print(i,end=" ")
        print()

    conn.close()



def one_books():
    conn = sqlite3.connect("sql_lite3/my_books.db")
    c = conn.cursor()
    c.execute("select * from books")
    book = c.fetchone()
    print(type(book))
    print(book)
    conn.close()



def big_books():
    conn = sqlite3.connect("sql_lite3/my_books.db")
    c = conn.cursor()
    c.execute("select title, pages from books where pages>300 order by pages desc")
    books = c.fetchall()

    for book in books:
        for i in book:
            print(i,end = " ")
        print()

    conn.close()



def update_books():
    conn = sqlite3.connect("sql_lite3/my_books.db")
    c = conn.cursor()
    sql = "update books set recommend = ? where title = ?"
    sql = "update books set recommend = :1 where title =:2"
    c.execute(sql,(200,'Java'))
    conn.commit()
    conn.close
    

def delete_books():
    conn = sqlite3.connect("sql_lite3/my_books.db")
    c = conn.cursor()

    sql = 'delete from books where publisher = "한빛"'
    c.execute(sql)
    conn.commit()
    conn.close()

