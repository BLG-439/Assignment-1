from flask import Flask, render_template, url_for
from forms import SignInForm

app=Flask(__name__)
app.config['SECRET_KEY']='f1cc00c7d395eab3b4c3'

@app.route('/')
def index():
  form = SignInForm()
  return render_template('signin.html', Hello="static/audio/hello.mp3", Signin_email="static/audio/sign_in1.mp3", Signin_password="static/audio/sign_in2.mp3", form=form)

@app.route('/kot')
def plot():
  return render_template('kot.html')

if __name__ == '__main__':
  app.run(debug=True)
