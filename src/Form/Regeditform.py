from flask_wtf import FlaskForm
from wtforms import TextField,PasswordField,SubmitField,validators,IntegerField

class Regeditform(FlaskForm):
    username = TextField('用户名：',[validators.Required('用户名必须输入')])
    password = PasswordField('密码：',[validators.Required('密码必须输入')])
    password_ = PasswordField('确认密码：',[validators.Required('请确认密码'),validators.EqualTo('password','两次输入的密码不一致')])
    age = IntegerField('年龄：',[validators.Required('年龄必须输入')])
    email = TextField('电子邮件：',[validators.Email('Email格式不正确')])
    telphone = TextField('联系电话：',[validators.Required('联系电话必须输入'),validators.Regexp('^[0-9]{11}$',message='联系电话位数错误')])
    submit = SubmitField('注册')
    submit_login = SubmitField('去登录')

