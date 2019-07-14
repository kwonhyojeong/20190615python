import pymysql

def cn_db():
    cn = pymysql.connect(host = 'localhost', 
                            user='root',
                            password='qwer1234',
                            db='test',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    return cn

def create_table():
    cn = cn_db()
    c = cn.cursor()
    c.execute('''
    create table if not exists users(
        userid varchar(11) not null,
        email varchar(255) not null,
        address varchar(255),
        password varchar(255) not null,
        primary key (userid)
    )''')
    
    cn.commit()
    cn.close()


def insert_users(user):
    cn = cn_db()
    c = cn.cursor()
    sql = 'insert into userid values(%s,%s,%s,%s)'
    c.execute(sql,user)

    cn.commit()
    cn.close()


def all_users():
    cn = cn_db()
    c = cn.cursor()
    c.execute("select * from users")

    print('[1] 전체 데이터 출력하기')

    users = c.fetchall()
    print(len(users))
    print(users)

    cn.close()

    return users


def one_user(userid):
    cn = cn_db()
    c = cn.cursor()
    sql = "select * from users where userid=%s"
    c.execute(sql,userid)
    user = c.fetchone()

    cn.commit()
    cn.close()
    
    return user