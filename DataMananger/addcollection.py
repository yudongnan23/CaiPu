from pymysql import *

def connectDB():
    db = connect('localhost','root','1234','cookbook',charset = 'utf8')
    return db

def addcollection(*list):
    db = connectDB()
    cursor = db.cursor()
    sql = '''INSERT INTO collection (user_id,cookbook_id,datetime) VALUE ({},{},'{}')'''.format(list[0],list[1],list[2])
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
        return '数据提交成功'
    except Exception as e:
        print(e)
        db.rollback()
        db.close()
    return '数据提交失败'
