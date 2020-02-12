from flask import Flask, render_template, url_for,flash, redirect, jsonify, request
from forms import Registration_From, LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = '61049065c85039da398f4ee7c2b81808'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
db.create_all()





@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"User('{self.id}', '{self.login}', '{self.email}', '{self.password}')"


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"Schedule('{self.id}', '{self.title}', '{self.description}')"





@app.route('/home')
def home():
    return render_template('hello.html')

@app.route('/register',methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = Registration_From()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        polzov = User(login=form.login.data, email=form.email.data, password=hashed_pw)
        log_test = User.query.filter_by(login=form.login.data).first()
        em_test = User.query.filter_by(login=form.email.data).first()
        if em_test:
            flash(f'This E-Mail alrealy exists. Please, change another one', 'error')
        if log_test:
            flash(f'This Login alrealy exists. Please, change another one', 'error')
        if em_test == None and log_test == None:
            db.session.add(polzov)
            db.session.commit()
            flash(f'Your account has been created. Now Log In!','success')
            return redirect(url_for('login'))
    return render_template('register.html', name='Register', form=form)

@app.route('/login',methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('schedule'))
        else:
            flash('Login unsuccessful. Please, check your Login or password','danger')
    return render_template('login.html', name='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/schedule', methods=['GET'])
def schedule_all():
    schedule_list = Schedule.query.all()
    output = []
    for sche in schedule_list:
        schedule_data = {}
        schedule_data['id'] = sche.id
        schedule_data['title'] = sche.title
        schedule_data['description'] = sche.description
        output.append(schedule_data)
    return jsonify ({'Schedule' : output})

@app.route('/schedule/<schedule_id>', methods=['GET'])
def schedule_one_raw(schedule_id):
    sched = Schedule.query.filter_by(id=schedule_id).first()
    if not sched:
        return jsonify({'message' : 'No schedule Found!'})
    sched_data = {}
    sched_data['id'] = sched.id
    sched_data['title'] = sched.title
    sched_data['description'] = sched.description
    return jsonify({'Schedule': sched_data})

@app.route('/schedule/<schedule_id>', methods=['DELETE'])
def schedule_remove_raw(schedule_id):
    sched = Schedule.query.filter_by(id=schedule_id).first
    if not sched:
        return jsonify({'message' : 'No schedule Found!'})
    db.session.delete(sched)
    db.session.commit()
    return jsonify({'message' : 'Schedule successfully deleted!'})

@app.route('/schedule', methods=['POST'])
def schedule_create():
    db.create_all()
    data = request.get_json()
    new_sche = Schedule(title=data['title'],description=data['description'])
    db.session.add(new_sche)
    db.session.commit()
    return jsonify({'Message' : 'New Schedule Created'})

@app.route('/schedule/<schedule_id>', methods=['PUT'])
def schedule_change(schedule_id):
    sched = Schedule.query.filter_by(id=schedule_id).first()
    if not sched:
        return jsonify({'message' : 'No schedule Found!'})
    else:
        data = request.get_json()
        if data['title']:
            sched.title = data['title']
        if data['description']:
            sched.description = data['description']
        db.session.commit()
        return jsonify({'Message' : 'Schedule Changed!'})


if __name__ == '__main__':
    app.run(debug=True)