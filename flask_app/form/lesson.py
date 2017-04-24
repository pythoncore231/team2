from wtforms import Form, StringField, IntegerField, validators

class LessonForm(Form):
    name = StringField('Name', [validators.Length(min=5, max=20)])
    teacher = IntegerField('teacher')