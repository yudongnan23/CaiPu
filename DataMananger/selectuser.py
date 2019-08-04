from pymysql import *

def connectDB():
    db = connect('localhost','root','1234','cookbook',charset = 'utf8')
    return db

def selectuser(username,password):
    db = connectDB()
    cursor = db.cursor()
    sql = '''SELECT id FROM user WHERE username='{}' AND password = '{}'  '''.format(username,password)
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result)==0:
            db.close()
            return False
        else:
            return True
            db.close()
    except Exception as e:
        db.close()
        print(e)


def userinform(username):
    db = connectDB()
    cursor = db.cursor()
    sql = ''' SELECT id,username,age,email,telphone,date FROM user WHERE username='{}' '''.format(username)
    try:
        cursor.execute(sql)
        result = cursor.fetchall()[0]
        db.close()
        return result
    except Exception as e:
        db.close()
        print(e)

def update(username,*list):
    db = connectDB()
    cursor = db.cursor()
    sql = ''' UPDATE user SET username='{}',age={},email='{}',telphone='{}' WHERE username='{}' '''.format(list[0],list[1],list[2],list[3],username)
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        db.close()
        print(e)
    return False
