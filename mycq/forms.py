from flask.ext.wtf import Form, TextField, Required, validators
from flask.ext.wtf.html5 import EmailField

class SignupForm(Form):
    name = TextField("Name", validators=[Required()])
    roll_no = TextField("Roll No", validators=[Required()])
    branch = TextField("Branch", validators=[Required()])
    email = EmailField("Email", validators=[Required(), validators.Email()])
