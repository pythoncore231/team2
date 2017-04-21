from wtforms import Form, StringField, IntegerField, validators

class UserForm(Form):
    firstname= StringField('First name', [validators.Length(min=2, max=10)])
    lastname = StringField('Last name', [validators.Length(min=2, max=10)])
    age = IntegerField('Age')