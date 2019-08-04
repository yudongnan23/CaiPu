from pymysql import *

def connectDB():
    db = connect('localhost','root','1234','cookbook',charset = 'utf8')
    return db

def deletecomment(id):
    db = connectDB()
    cursor = db.cursor()
    sql = 'DELETE FROM comment WHERE id = {}'.format(id)
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
        return '数据删除成功'
    except Exception as e:
        print(e)
        db.rollback()
        db.close()
    return '数据删除失败'
