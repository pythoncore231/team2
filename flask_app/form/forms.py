from wtforms import Form, StringField, IntegerField, validators, TextAreaField, SelectField

class RoomForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=10)])
    capacity = IntegerField('Capacity')

class UserForm(Form):
    firstname= StringField('First name', [validators.Length(min=1, max=5)])
    lastname = StringField('Last name', [validators.Length(min=10, max=20)])
    age = IntegerField('Age')
    group = SelectField('Group', choices=[('Team1', 'team1'),('Team2', 'team2')]) # need to get from db existing groups

class GroupForm(Form):
    groupname= StringField('Group name', [validators.Length(min=1, max=5)])
    members = TextAreaField('Members') #need to get from existing members

class TeacherForm(Form):
    position= StringField('Position', [validators.Length(min=1, max=5)])

class LessonForm(Form):
    lesson_name= StringField('Lesson name', [validators.Length(min=1, max=5)])
    teacher = IntegerField('teacher id')

class ScheduleForm(Form):
    room_name= StringField('Lesson name', [validators.Length(min=1, max=5)])
    lesson_name= StringField('Lesson name', [validators.Length(min=1, max=5)])
    group_name= StringField('Lesson name', [validators.Length(min=1, max=5)])
    para = StringField('Teacher', [validators.Length(min=10, max=20)])
