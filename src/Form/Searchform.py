from flask_wtf import FlaskForm
from wtforms import SubmitField

class Searchform(FlaskForm):
    submit_sc = SubmitField('收藏',id = 'sc')
    submit_sc_click = SubmitField('已收藏',id='sc_click')
