from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SelectField, PasswordField
from wtforms.validators import DataRequired, Required, EqualTo
from ctfscore import models, db



class InputFlag(Form):
    user    = StringField(u'user', validators=[DataRequired()])
    flag    = StringField(u'flag', validators=[DataRequired()])

