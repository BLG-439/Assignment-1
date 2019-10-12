from flask import Flask, render_template, url_for, redirect
from forms import SignInForm

#Borrowed
from k import get_messages


app=Flask(__name__)
app.config['SECRET_KEY']='f1cc00c7d395eab3b4c3' #10

@app.route('/', methods=['GET', 'POST'])
def index():
  form = SignInForm()
  if form.validate_on_submit():
    messages=get_messages(form.email.data, form.password.data)
    return render_template('loggedin.html', Messages=messages)
  return render_template('signin.html', Hello="static/audio/hello.mp3", Signin_email="static/audio/sign_in1.mp3", Signin_password="static/audio/sign_in2.mp3", form=form)

if __name__ == '__main__':
  app.run(debug=True)
