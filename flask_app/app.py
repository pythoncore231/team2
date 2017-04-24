import os.path

from flask import Flask, request, redirect,  render_template
from flask_sqlalchemy import SQLAlchemy

from form.room import RoomForm
from form.user import UserForm
from form.lesson import LessonForm
from form.scheduler import SchedulerForm

app = Flask(__name__, static_url_path = "", static_folder = "static")#

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')

def get_resource_as_string(name, charset='utf-8'):
    with app.open_resource(name) as f:
        return f.read().decode(charset)

app.jinja_env.globals['get_resource_as_string'] = get_resource_as_string

db = SQLAlchemy(app)


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        data = {}
        data["id"] = self.id
        data["name"] = self.name
        data["capacity"] = self.capacity

        return data

    def __repr__(self):
        return '<Room {} {}>'.format(self.name, self.capacity)

    @staticmethod
    def get_room(id):
        room = None
        try:
            room = Room.query.get(id)
        except Exception, e:
            print e
        return room

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=True)

    @staticmethod
    def get_user(id):
        user = None
        try:
            user = User.query.get(id)
        except Exception, e:
            print e
        return user

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    teacher = db.Column(db.Integer, nullable=False)

    def get_teacher(self):
        return User.get_user(self.teacher)

    def to_dict(self):
        data = {}
        data["id"] = self.id
        data["name"] = self.name
        data["teacher"] = User.query.get(self.teacher).firstname

        return data

    def __repr__(self):
        return '<Lesson {} {} {}>'.format(self.id, self.name, self.teacher)

class Scheduler(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, nullable=False)
    lesson_id = db.Column(db.Integer, nullable=False)
    # group_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    para = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        data = {}
        data["id"] = self.id
        data["room"] = Room.query.get(self.room_id).name
        # data["room"] = Room.get_by_id(self.room_id)
        data["lesson"] = Lesson.query.get(self.lesson_id).name
        # data["lesson"] = Lesson.get_by_id(self.lesson_id)
        # data["group"] = Group.get_by_id(self.group_id)
        data["date"] = self.date
        data["para"] = self.para

        return data

    def __repr__(self):
        return '<Lesson {} {} {}>'.format(self.id, self.name, self.teacher)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/test')
def hello_world_test():
    return 'test Hello, World!'

@app.route('/room', methods=['GET', 'POST'])
def room():
    form = RoomForm(request.form)
    if request.method == 'POST' and form.validate():
        room = Room(name=form.name.data, capacity=form.capacity.data)
        db.session.add(room)
        db.session.commit()
        return redirect('/room')

    rooms = Room.query.all()
    return render_template('room.html', form=form, rooms=rooms)

@app.route('/user', methods=['GET', 'POST'])
def user_get():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(firstname=form.firstname.data,
                    lastname=form.lastname.data,
                    age=form.age.data)
        db.session.add(user)
        db.session.commit()
        return redirect('/user')

    users = User.query.all()
    return render_template('user.html', form=form, users=users)

@app.route('/lesson', methods=['GET','POST'])
def lesson_get_post():
    form = LessonForm(request.form)
    if request.method == 'POST' and form.validate():
        lesson = Lesson(name = form.name.data,
                        teacher = form.teacher.data)
        db.session.add(lesson)
        db.session.commit()
        return redirect('/lesson')
    users = User.query.all()
    lessons = Lesson.query.all()
    for lesson in lessons:
        lesson.teacher = lesson.get_teacher()
    return render_template('lesson.html', form=form, users=users, lessons=lessons)

@app.route('/scheduler', methods=['GET','POST'])
def scheduler_get_post():
    form = SchedulerForm(request.form)
    if request.method == 'POST' and form.validate():
        scheduler =  Scheduler(room_id = form.room_id.data,
                               lesson_id = form.lesson_id.data,
                               date = form.date.data,
                               para = form.para.data)
        db.session.add(scheduler)
        db.session.commit()
        return redirect('/scheduler')

    users = User.query.all()
    lessons = [s.to_dict() for s in Lesson.query.all()]
    rooms = Room.query.all()
    schedulers = [s.to_dict() for s in Scheduler.query.all()]
    # print schedulers
    return render_template('scheduler.html', form=form, schedulers=schedulers,
                           users=users, lessons=lessons, rooms=rooms)

if __name__ == "__main__":
    db.create_all()
    app.run()
