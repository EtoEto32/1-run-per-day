from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///sample.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO']=True  #ログ出力
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)

# 一度実行するとテーブルが作成される
with app.app_context():
    db.create_all()
    
@app.route('/', methods=['GET'])
def index():
    users =db.session.query(User).all()
    return render_template('index.html', users = users)

@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        user = User(name=name, age=age)
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('create.html')

@app.route('/<int:id>/update', methods=['GET','POST'])
def update(id):
    user = db.session.get(User, id)
    if request.method == 'GET':
        return render_template('update.html',post=user)
    else:
        user.name = request.form.get('name')
        user.age = request.form.get('age')
        db.session.commit()
        return redirect('/')

@app.route('/<int:id>/delete', methods=['GET'])
def delete(id):
    user = db.session.get(User, id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/')

    
if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost') 