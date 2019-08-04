import re
from DataMananger.selectcookbook import selectcookbook_bytitle

def change(title):
    list = []
    text = selectcookbook_bytitle(title)[0]
    for item in re.split('\r\n',text[6]):
        list.append(item)
    return list


