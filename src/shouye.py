from flask import Flask,render_template,request,session,redirect
from flask_bootstrap import Bootstrap
from src.Form.Loginform import MyForm
from src.Form.Regeditform import Regeditform
from DataMananger.selectuser import selectuser
from src.Form.Userform import UserForm
from DataMananger.selectuser import userinform,update
from DataMananger.adduser import insertusers
from src.exchangetime import timeexchange
from DataMananger.selectcookbook import selectcookbook
from src.Form.Shouyeform import Shouyeform
from DataMananger.selectcookbook import selectcookbook_bytitle,add_zan
from src.Form.Searchform import Searchform
from DataMananger.collection import collectionclass
from DataMananger.selectcollection import selectcollection,deletecollection
import json
from src.textchange import change
from DataMananger.selectcomment import cookbook_selectcomment
from urllib import parse


app = Flask(__name__)
app.secret_key = 'Antetokounmpo34'
bootstrap = Bootstrap(app)

list_sy = selectcookbook()
# 根路由
@app.route('/')
def index():
    shouyeform = Shouyeform()
    if 'username' in session:
        ok = True
        return render_template('shouye.html',username = session['username'],ok = ok,list=list_sy,form = shouyeform)
    else:
        return render_template('shouye.html',list=list_sy,form = shouyeform)




# 登录路由
@app.route('/login',methods = ['GET','POST'])
def login():
    shouyeform = Shouyeform()
    form = MyForm()
    ok = False
    flag = False
    if request.method == 'POST':
        if form.validate_on_submit() == False:
            print('error')
        else:
            username = form.username.data
            password = form.password.data
            if selectuser(username,password):
                session['username']=username
                ok = True
                return render_template('shouye.html',ok = ok,username = username,list=list_sy,form = shouyeform)
            else:
                flag = True
                return render_template('login.html',form=form,flag=flag)
    return render_template('login.html',form = form,ok = ok)

# 注册路由
@app.route('/regedit',methods = ['GET','POST'])
def regedit():
    form = Regeditform()
    ok = False
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.submit.data:
                user = [form.username.data,form.password.data,form.age.data,form.email.data,form.telphone.data,timeexchange()]
                ok = insertusers(*user)
    return render_template('regedit.html',form = form,ok = ok)

# 用户路由
@app.route('/user',methods = ['GET','POST'])
def userinformation():
    shouyeform = Shouyeform()
    if 'username' in session:
        form = UserForm()
        ok = False
        flag = False
        if request.method == 'POST':
            if form.validate_on_submit():
                if form.update.data:
                    username = form.username.data
                    print(username)
                    age = form.age.data
                    email = form.email.data
                    telphone =form.telphone.data
                    list_update = [username,age,email,telphone]
                    ok = update(session['username'],*list_update)
                    print(list_update)
                    session['username'] = username
                if form.loginout.data:
                    session.pop('username',None)
                    flag = True
                    return render_template('shouye.html',flag=flag,list=list_sy,form = shouyeform)
        list = userinform(session['username'])
        form.username.data = list[1]
        form.age.data = list[2]
        form.email.data = list[3]
        form.telphone.data = list[4]
        form.date.data = list[5]
        return render_template('user.html',form=form,username=session['username'],ok = ok,flag = flag)
    else:
        fg = True
        return render_template('shouye.html',list=list_sy,form = shouyeform,fg = fg)


# 向前端传送视频示例
@app.route('/vedio')
def vedio():
    return redirect('/static/hello.mp4')


# 展开更多
@app.route('/more')
def more():
    ok = False
    if 'username' in session:
        ok = True
        return render_template('more.html',search_name = '可乐鸡翅',ok = ok,username = session['username'],list = list_sy)
    else:
        return render_template('more.html',search='可乐鸡翅',ok = ok,list = list_sy     )

# 搜索路由
@app.route('/search',methods = ['GET','POST'])
def search():
    searchform = Searchform()
    search_name = request.args.get('search_name')
    books = selectcookbook_bytitle(search_name)
    ok = False
    sc_picture = 'sc.png'
    sc_word = '收藏'
    username_ok = False
    zan_picture = 'zan.png'
    if 'username' in session:
        username_ok = True
        user_id = userinform(session['username'])[0]
        if books:
            cookbook_id = selectcookbook_bytitle(search_name)[0][0]
            textlist = change(search_name)
            comments = cookbook_selectcomment(books[0][0])
            ok = True
            book = books[0]
            if collectionclass(user_id,cookbook_id).is_collection():
                sc_picture = 'sc_click.png'
                sc_word = '已收藏'
            return render_template('search.html',search_name = search_name,username = session['username'],
                                   book = book,username_ok = username_ok,ok = ok,sc_picture = sc_picture,
                                   sc_word = sc_word,zan_picture = zan_picture,textlist = textlist,comments = comments
                                )
        else:
            return render_template('search.html',search_name = search_name,username = session['username'],username_ok = username_ok,ok = ok)
    else:
        if books:
            textlist = change(search_name)
            comments = cookbook_selectcomment(books[0][0])
            ok = True
            book = books[0]
            return render_template('search.html',search_name = search_name,
                                   book = book,ok = ok,sc_picture = sc_picture,sc_word = sc_word,
                                   username_ok = username_ok,zan_picture = zan_picture,textlist = textlist,comments = comments

                                   )
        else:
            return render_template('search.html',search_name = search_name,ok = ok,sc_picture = sc_picture,sc_word = sc_word,username_ok = username_ok)


#定义点击收藏按钮接收ajax请求数据的路由
@app.route('/sc_click',methods = ['GET','POST'])
def sc_click():
    sc = request.form['sc_click']
    title = request.form['book_title']
    # 或取用户id
    user_id = userinform(session['username'])[0]
    # 获取菜谱id
    cookbook_id = selectcookbook_bytitle(title)[0][0]
    # 检验收藏是否存在
    if collectionclass(user_id = user_id,cookbook_id = cookbook_id).delete_collection():
        pass
    else:
        print(collectionclass(user_id = user_id,cookbook_id = cookbook_id).add_collection())
    return json.dumps({"code":"OK"})

# 定义赞的路由
@app.route('/zan',methods = ['GET','POST'])
def zan_click():
    title = request.form['book_title']
    zan_number = request.form['zan_number']
    add_zan(title,str(int(zan_number)+1))
    return json.dumps({"code":"OK"})

#定义我的收藏的路由
@app.route('/collection',methods = ['GET','POST'])
def collection():
    if 'username' in session:
        ok = True
        collections = selectcollection(session['username'])
        return render_template('collection.html',collections = collections,username = session['username'],ok = ok)
    else:
        fg = True
        shouyeform = Shouyeform()
        return render_template('shouye.html',list=list_sy,form = shouyeform,fg = fg)

#定义获取评论的数据
@app.route('/add_comment',methods = ['GET','POST'])
def add_comment():
    comment = request.form['comment']
    title = request.form['title']
    print(comment)
    print(title)
    return json.dumps({'code':'OK'})

#定义ajax动态请求删除收藏的路由
@app.route('/delete_collection',methods = ['GET','POST'])
def delete_collection():
    id = request.form['id']
    deletecollection(id)
    return json.dumps({'code':'OK'})


# 赣菜路由
@app.route('/gancai',methods = ['GET','POST'])
def gancai():
    return render_template('gancai.html')
# 川菜路由
# 湘菜路由
# 浙菜路由

# 启动所有路由函数
if __name__ == '__main__':
    app.run()
