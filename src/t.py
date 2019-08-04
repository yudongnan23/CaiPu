from src.exchangetime import timeexchange
from DataMananger.selectuser import *
from DataMananger.selectcookbook import selectcookbook_bytitle,add_zan
from DataMananger.selectcomment import cookbook_selectcomment
import re
from DataMananger.selectcollection import selectcollection,deletecollection

#print(collection(user_id=1,cookbook_id=1).delete_collection())
#print(userinform('MrYu'))
# list = []
# t = re.split('\r\n',selectcookbook_bytitle('可乐鸡翅')[0][6])
# for item in t:
    # list.append(item)
# for l in list:
    # print(l)
#print(add_zan('可乐鸡翅','667'))

# id = selectcookbook_bytitle('可乐鸡翅')[0][0]
# print(id)
# comment =  cookbook_selectcomment(id)
# print(comment[0][3])
print(selectcollection('MrYU'))

