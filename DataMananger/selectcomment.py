from pymysql import *

def connectDB():
    db = connect('localhost','root','1234','cookbook',charset = 'utf8')
    return db

def user_selectcomment(user_id):
    db = connectDB()
    cursor = db.cursor()
    sql = '''SELECT content ,cookbook_id,date FROM comment WHERE user_id={}'''.format(user_id)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        db.close()
        return results
    except Exception as e:
        print(e)
        db.close()
    return '查询失败'

def cookbook_selectcomment(cookboo_id):
    db = connectDB()
    cursor = db.cursor()
    sql = '''SELECT username,content ,comment.user_id,comment.date FROM user,comment WHERE cookbook_id={} and user.id = comment.user_id'''.format(cookboo_id)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        db.close()
        return results
    except Exception as e:
        print(e)
        db.rollback()
        db.close()
    return '暂时没有评论'
