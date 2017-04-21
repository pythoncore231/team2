from wtforms import Form, StringField, IntegerField, validators
from wtforms.fields.html5 import DateField

class RoomForm(Form):
    name = StringField('Name', [validators.Length(min=3, max=5)])
    capacity = IntegerField('Capacity')


class UserForm(Form):
    firstname= StringField('First name', [validators.Length(min=1, max=20)])
    lastname = StringField('Last name', [validators.Length(min=1, max=20)])
    age = IntegerField('Age')



class LessonForm(Form):
    name = StringField('Name', [validators.Length(min=5, max=20)])
    teacher = IntegerField('teacher')

class SchedulerForm(Form):
    room_id = IntegerField('room_id')
    lesson_id = IntegerField('lesson_id')
    # group_id = IntegerField('group_id')
    date = DateField("date", format='%Y-%m-%d')
    para = IntegerField('group_id')