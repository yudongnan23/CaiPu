from pymysql import *

def connectDB():
    db = connect('localhost','root','1234','cookbook',charset = 'utf8')
    return db

def selectcookbook():
    db = connectDB()
    cursor = db.cursor()
    sql = '''SELECT id,imageurl,title,class,deepclass FROM cookbook'''
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

def selectbook_byId(cookbook_id):
    db = connectDB()
    cursor = db.cursor()
    sql = '''SELECT title,class FROM cookbook where id = {}'''.format(cookbook_id)
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

def selectcookbook_bytitle(title):
    db = connectDB()
    cursor = db.cursor()
    sql = ''' Select id,title,imageurl,videourl,class ,zan ,words from cookbook where title = "{}"'''.format(title)
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        db.close()
        return result
    except Exception as e:
        print(e)
        db.rollback()
        db.close()
    return '查询失败'

def add_zan(title,zan_number):
    db = connectDB()
    cursor = db.cursor()
    sql = ''' update cookbook SET zan = '{}'where title = '{}' '''.format(zan_number,title)
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        db.close()
    return False

