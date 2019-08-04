from pymysql import *

def connectDB():
    db = connect('localhost','root','1234','cookbook',charset = 'utf8')
    return db

def selectcollection(username):
    db = connectDB()
    cursor = db.cursor()
    sql = '''SELECT title,datetime,cookbook.imageurl,collection.id FROM collection,user,cookbook WHERE username = '{}' and user.id = collection.user_id and collection.cookbook_id = cookbook.id'''.format(username)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        db.close()
        return results
    except Exception as e:
        print(e)
        db.rollback()
        db.close()
    return '数据查询失败'

# 用户删除收藏
def deletecollection(id):
     db = connectDB()
     cursor = db.cursor()
     sql  = ''' delete from collection where id = {} '''.format(id)
     try:
         cursor.execute(sql)
         db.commit()
         db.close()
         return True
     except Exception as e:
         db.rollback()
         db.close()
     return False
