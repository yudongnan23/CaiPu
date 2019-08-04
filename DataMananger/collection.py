from pymysql import *
from src.exchangetime import timeexchange

class collectionclass:
    def __init__(self,user_id,cookbook_id):
        self.user_id = user_id
        self.cookbook_id = cookbook_id
        self.datetime = timeexchange()
        self.db = connect('localhost','root','1234','cookbook',charset = 'utf8')

    #用戶添加收藏记录
    def add_collection(self):
        cursor = self.db.cursor()
        sql = ''' INSERT INTO collection(user_id,cookbook_id,datetime) VALUES({},{},'{}')'''.format(self.user_id,self.cookbook_id,self.datetime)
        try:
            cursor.execute(sql)
            self.db.commit()
            self.db.close()
            return True
        except Exception as e:
            self.db.rollback()
            self.db.close()
        return 'Fail'

    #用户取消收藏
    def delete_collection(self):
        cursor = self.db.cursor()
        sql = ''' SELECT user_id,cookbook_id FROM collection WHERE user_id = {} and cookbook_id = {}'''.format(self.user_id,self.cookbook_id)
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception as e:
            self.db.rollback()
            self.db.close()
            return False
        if len(result) == 1:
            sql2 = ''' delete from collection where user_id = {} and cookbook_id = {} '''.format(self.user_id,self.cookbook_id)
            try:
                cursor.execute(sql2)
                self.db.commit()
                self.db.close()
                return True
            except Exception as e:
                self.db.rollback()
                self.db.close()
        return False

    # 检验是否收藏
    def is_collection(self):
        cursor = self.db.cursor()
        sql = '''SELECT user_id,cookbook_id FROM collection WHERE user_id = {} and cookbook_id = {}'''.format(self.user_id,self.cookbook_id)
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            self.db.close()
        except Exception as e:
            self.db.rollback()
            self.db.close()
        if len(result) == 1:
            return True
        else:
            return False




