from wtforms import Form, TextField

class UserForm(Form):
    username = TextField('Username')
