from wtforms import Form, StringField, IntegerField, validators

class RoomForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=10)])
    capacity = IntegerField('Capacity')


class UserForm(Form):
    firstname = StringField('First name', [validators.Length(min=1, max=5)])
    lastname = StringField('Last name', [validators.Length(min=10, max=20)])
    age = IntegerField('Age')
    


class TeacherForm(Form):
    firstname = StringField('First name', [validators.Length(min=1, max=5)])
    lastname = StringField('Last name', [validators.Length(min=10, max=20)])
    age = IntegerField('Age')
    position = StringField('Position', [validators.Length(min=1, max=20)])


# class LessonForm(Form):
#     name = StringField('Name', [validators.Length(min=1, max=10)])
#     firstname = StringField('First name', [validators.Length(min=1, max=5)])
#     lastname = StringField('Last name', [validators.Length(min=10, max=20)])
#     age = IntegerField('Age')
#     position = StringField('Position', [validators.Length(min=1, max=20)])


# class GroupForm(Form):
#     name = StringField('Name', [validators.Length(min=1, max=10)])
#     firstname = StringField('First name', [validators.Length(min=1, max=5)])
#     lastname = StringField('Last name', [validators.Length(min=10, max=20)])
#     age = IntegerField('Age')











