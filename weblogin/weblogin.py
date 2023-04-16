import html
from flask import Flask, render_template, request
from DBcm import UseDatabase

app = Flask(__name__)

dbconfig = {'host': '0.0.0.0',
            'port': 33060,
            'user': 'ariel',
            'password':'kaiosama',
            'database': 'webapp',}

@app.route('/')
@app.route('/login', methods=['POST'])
def login() -> 'html':
    return render_template('login.html',
                           the_title ='Login please!')
@app.route('/forgpass')
def pass_recovery() -> 'html':
    return render_template('forgpass.html',
                           the_title ='Password Recovery',)

@app.route('/signup')
def signup_form() -> 'html':
    return render_template('signup.html',
                           the_title ='SignUp Form',)

@app.route('/status', methods=['POST'])
def view_the_log() -> 'html':
    uname = request.form['username']
    upass = request.form['userpass']
    with UseDatabase(dbconfig) as cursor:
        _SQL = f"""SELECT username, userpwd, role
        FROM user
        WHERE username='{uname}'"""
        cursor.execute(_SQL)
        row = cursor.fetchone()

        if row == None:
            return render_template('status.html',
                        the_title='User Not Found!',
                        )
        elif row[1] != upass:
            return render_template('status.html',
            the_title='Wrong Password!',
            )
  
    return render_template('status.html',
                           the_title=f'Welcome {uname}',
                           user_name = uname,
                           role= row[2],)

if __name__ == '__main__':
    app.run(debug=True)