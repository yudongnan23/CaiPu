from flask_wtf import FlaskForm
from wtforms import TextField,SubmitField,validators,IntegerField

class Shouyeform(FlaskForm):
    search = TextField([validators.Required('请输入搜索关键词')])
    submit = SubmitField('搜索')
    submit_more = SubmitField('加载更多...',id='more')
