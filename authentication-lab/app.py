from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {
  "apiKey": "AIzaSyAG81cxeR_E7vYaamDZT2fmArx3OGMgVCg",
  "authDomain": "dinosaurcake-ba4e5.firebaseapp.com",
  "projectId": "dinosaurcake-ba4e5",
  "storageBucket": "dinosaurcake-ba4e5.appspot.com",
  "messagingSenderId": "466473887088",
  "appId": "1:466473887088:web:b19c5b649fcfe41116dbb5",
  "databaseURL": ""
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    error=""
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
        login_session['user'] = auth.create_user_with

    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)