from flask import Flask, render_template,request, redirect, g
from flask_bootstrap import Bootstrap
import sqlite3

app = Flask(__name__)
bootstrap = Bootstrap(app)

def get_db():
    # print(type(g))
    db = getattr(g, '_database', None)
    if db is None:
        db = g._databese  = sqlite3.connect('sample.db')
    return db

    
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/', methods=['GET'])
def index():
    con = get_db()
    cur = con.execute("SELECT * FROM user ORDER BY id")
    users = cur.fetchall()
    return render_template('index.html', users = users)

@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == "POST":
        name = request.form.get('name')
        age = request.form.get('age')
        con = get_db()
        sql = f"INSERT INTO user(name, age) values('{name}',{age})"
        con.execute(sql)
        con.commit()
        return redirect('/')
    else:
        return render_template('create.html')

@app.route('/<int:id>/update', methods=['GET','POST'])
def update(id):
    con = get_db()
    cur = con.execute(f"SELECT * FROM user WHERE id = {id}")
    user = cur.fetchone()
    if request.method == "GET":
        return render_template('update.html',post=user)
    else:
        name = request.form.get('name')
        age = request.form.get('age')
        sql = f"UPDATE user SET name = '{name}', age = {age} WHERE id ={id}"
        con.execute(sql)
        con.commit()
        return redirect('/')

@app.route('/<int:id>/delete', methods=['GET'])
def delete(id):
    con = get_db()
    sql = f"DELETE FROM user WHERE id ={id}"
    con.execute(sql)
    con.commit()
    return redirect('/')

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost') 