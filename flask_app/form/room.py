from wtforms import Form, StringField, IntegerField, validators

class RoomForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=10)])
    capacity = IntegerField('Capacity')


class UserForm(Form):
    firstname= StringField('First name', [validators.Length(min=1, max=5)])
    lastname = StringField('Last name', [validators.Length(min=10, max=20)])
    age = IntegerField('Age')
