from pymysql import *

def connectDB():
    db = connect('localhost','root','1234','cookbook',charset = 'utf8')
    return db

def insertcomment(*comment):
    db = connectDB()
    cursor = db.cursor()
    sql = ''' INSERT INTO comment(content,user_id,cookbook_id,date) VALUES ('{}',{},{},'{}')'''.format(comment[0],comment[1],comment[2],comment[3])
    try:
        cursor.execute(sql)
        db.commit()
        return '数据提交成功'
    except Exception as e:
        print(e)
        db.rollback()
        db.close()
    return '数据提交失败'

