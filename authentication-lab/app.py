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
  "databaseURL": "https://dinosaurcake-ba4e5-default-rtdb.europe-west1.firebasedatabase.app/"
}

user = {
    
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    error=""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email,password)
            return redirect(url_for('add_tweet'))
        except:
            error = "Authentication failed"
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error=""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email,password)
            user['full_name'] = request.form['full_name'] 
            user['username'] = request.form['username']
            user['bio'] = request.form['bio']
            db.child("user1").push(user)
            return redirect(url_for('add_tweet'))
        except:
            error = "Authentication failed"
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    if request.method == 'POST':
       try:
           tweet = {"title": request.form['title'],
                      "text": request.form['text']}
           db.child("tweets").push(tweet)
       except:
           print("Couldn't add book")

    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)