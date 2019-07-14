import pymysql

def conn_db():
    conn = pymysql.connect(host = 'localhost', 
                            user='root',
                            password='qwer1234',
                            db='test',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor
    )
    return conn

def create_table():
    conn = conn_db()
    c = conn.cursor()
    c.execute('''
    create table if not exists books(
        title text,
        purblished_date text,
        publisher text,
        pages integer,
        recommend integer
    )''')
    
    conn.commit()
    conn.close()

def insert_books():
    conn = conn_db()
    c = conn.cursor()

    # c.execute("insert into books values('Java','2019-05-20','길벗',500,10)")
    sql='insert into books values(%s,%s,%s,%s,%s)'
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
    cn = conn_db()
    c=cn.cursor()
    c.execute("select * from books")

    print('[1] 전체 데이터 출력하기')

    books = c.fetchall()
    print(type(books))
    print(len(books))
    print(books)

    for book in books:
        for i in book:
            print(book[i],end=" ")
        print()

    cn.close()

def some_books(number):
    cn = conn_db()
    c = cn.cursor()
    c.execute("select * from books")
    books = c.fetchmany(number)

    for book in books:
        for i in book:
            print(book[i],end=" ")
        print()
    cn.close()

def update_books():
    cn = conn_db()
    c = cn.cursor()
    sql = 'update books set recommend = %s where title = %s'
    c.execute(sql,(200,'Java'))
    cn.commit()
    cn.close()

def delete_books():
    cn = conn_db()
    c = cn.cursor()
    sql = "delete from books where publisher = '한빛'"
    c.execute(sql)

    cn.commit()
    cn.close()