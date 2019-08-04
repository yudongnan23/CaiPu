from flask_wtf import FlaskForm
from wtforms import TextField,PasswordField,SubmitField,validators,BooleanField
from wtforms.validators import DataRequired
class MyForm(FlaskForm):
    username = TextField('用户名：',validators = [DataRequired('请输入用户名')])
    password = PasswordField('密码：',validators = [DataRequired('请输入密码')])
    remenber = BooleanField('记住密码',default=False)
    submit_login = SubmitField('登录')
