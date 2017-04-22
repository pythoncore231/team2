import os.path

from flask import Flask, request, redirect,  render_template
from flask_sqlalchemy import SQLAlchemy

from form.forms import RoomForm, UserForm, LessonForm

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')

db = SQLAlchemy(app)


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Room {} {}>'.format(self.name, self.capacity)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    group = db.Column(db.String(20), nullable=False)
    
    @staticmethod
    def get_user(id):
        try:
            user = User.query.get(id)
        except Exception, e:
            return e
        finally:
            pass

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    teacher = db.Column(db.Integer, nullable=False)

    def getValue(self):
        self.teacher = User.get_user(self.teacher)


@app.route('/')
def hello_world():
    return """
            <a href='http://localhost:5000/user'>list users</a><br>
            <a href='http://localhost:5000/user/add'>add user</a><br>
            <a href='http://localhost:5000/room'>edit rooms</a><br>
            <a href='http://localhost:5000/group'>edit groups</a><br>
            <a href='http://localhost:5000/teacher'>edit teachers</a><br>
            <a href='http://localhost:5000/lesson'>edit lessons</a><br>
            <a href='http://localhost:5000/scheduler'>get schedule</a>"""

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



@app.route('/user', methods=['GET'])
def user_get():
    users = User.query.all()
    return render_template('user.html', us=users)

@app.route('/user/add', methods=['GET','POST'])
def user_add():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(firstname = form.firstname.data,
                    lastname = form.lastname.data,
                    age = form.age.data,
                    group = form.group.data)
        db.session.add(user)
        db.session.commit()
        return redirect('/user')
    return render_template('user_add.html', form=form)

@app.route('/user/<id>/update', methods=['GET','POST'])
def user_update(id):
    user = User.get_user(id)
    if user:
        if request.method == "POST":
            user.firstname = form.firstname.data
            user.lastname = form.firstname.data
            user.age = form.age.data
            user.group = form.group.data
            db.session.commit()
        form.firstname.data = user.firstname
        form.lastname.data = user.lastname
        form.age.data = user.age
        form.group.data = user.group
        return render_template("user_update.html", form=form)
    return redirect('/user')

    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(firstname = form.firstname.data,
                    lastname = form.lastname.data,
                    age = form.age.data,
                    group = form.group.data)
        db.session.add(user)
        db.session.commit()
        return redirect('/user')
    return render_template('user_add.html', form=form)

@app.route('/user/lesson', methods=['GET','POST'])
def lessons(id):
    user = User.querry.all()
    lessons = Lesson.querry.all()
    form = LessonForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(firstname = form.firstname.data,
                    lastname = form.lastname.data,
                    age = form.age.data,
                    group = form.group.data)
        db.session.add(user)
        db.session.commit()
        return redirect('/user')


if __name__ == "__main__":
    db.create_all()
    app.run()
