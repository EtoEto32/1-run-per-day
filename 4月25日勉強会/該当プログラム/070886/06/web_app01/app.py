from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return '<p>Hello, World!</p>'

@app.route('/user/<int:id>')
def hello_user(id):
    return render_template('hello.html', id=id)
    # return f'<p>Hello, User. Your ID is {id}.</p>'

# @app.route('/flask')
# def hello_flask():
#     return '<p>Hello, Flask!</p>'

# @app.route('/python')
# def hello_python():
#     return '<p>Hello, Python</p>'