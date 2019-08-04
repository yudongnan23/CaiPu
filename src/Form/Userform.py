from flask_wtf import FlaskForm
from wtforms import TextField,SubmitField,validators,IntegerField

class UserForm(FlaskForm):
    username = TextField('用户名:',[validators.Required('修改用户名时请勿输入空的用户名')])
    age = IntegerField('年龄:',[validators.Required('修改年龄时请勿输入空的年龄')])
    email = TextField('电子邮件:',[validators.Email('Email格式不正确')])
    telphone = TextField('联系电话:',[validators.Required('修改联系电话时请勿输入空的联系电话'),validators.Regexp('^[0-9]{11}$',message='联系电话格式有误')])
    date = TextField('注册时间:')
    update = SubmitField('提交修改')
    loginout = SubmitField('退出登录')

