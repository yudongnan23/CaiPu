from pymysql import *


def connectDB():
    db = connect('localhost','root','1234','cookbook',charset = 'utf8')
    return db


def insertusers(*user):
    db = connectDB()
    cursor=db.cursor()
    sql = '''INSERT INTO user (username,password,age,email,telphone,date) VALUES ('{}','{}',{},'{}','{}','{}')'''.format(user[0],user[1],user[2],user[3],user[4],user[5])
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
        return True
    except Exception as e:
        print(e)
        db.rollback()
        db.close()
    return False


