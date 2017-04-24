from wtforms import Form, StringField, IntegerField, validators
from wtforms.fields.html5 import DateField

class SchedulerForm(Form):
    room_id = IntegerField('room_id')
    lesson_id = IntegerField('lesson_id')
    # group_id = IntegerField('group_id')
    date = DateField("date", format='%Y-%m-%d')
    para = IntegerField('group_id')