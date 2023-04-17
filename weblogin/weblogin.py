import html
from flask import Flask, render_template, request, flash
from DBcm import UseDatabase

app = Flask(__name__)
app.secret_key ="password1234"

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
        _SQL = f"""SELECT name, lastname, username, userpass, role
        FROM users
        WHERE username='{uname}'"""
        cursor.execute(_SQL)
        row = cursor.fetchone()

        if row == None:
            flash('User not created!', 'Warning')
            return render_template('status.html',
                        the_title='User Not Found!',
                        )
        elif row[3] != upass:
            flash('Invalid Password!', 'Error')
            return render_template('status.html',
            the_title='Wrong Password!',
            )
    flash('Your are logged in!', 'Info')
    return render_template('status.html',
                           the_title=f'Welcome {row[0]}',
                           user_name = uname,
                           role= row[4],)

if __name__ == '__main__':
    app.run(debug=True)