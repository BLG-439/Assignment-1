from flask import Flask, render_template, url_for, redirect, session
from forms import SignInForm, SendEmailForm, ReadFolderForm

#Borrowed
from k import get_messages, send_email


app=Flask(__name__)
app.config['SECRET_KEY']='f1cc00c7d395eab3b4c3' #10


@app.route('/', methods=['GET', 'POST'])
def index():
  sign_in_form = SignInForm()
  send_email_form = SendEmailForm()
  read_folder_form = ReadFolderForm()

  if sign_in_form.validate_on_submit():
    session.get('Email', sign_in_form.email.data)
    session.get('Password', sign_in_form.password.data)
    messages=get_messages(sign_in_form.email.data, sign_in_form.password.data)
    session.get('Messages', messages)
    return render_template('loggedin.html', Messages=messages, SendEmailForm=send_email_form) #Messages supozohet te jene te gjith mesazhet e marra

  if send_email_form.validate_on_submit():
    send_email(session['Email'], session['Password'], send_email_form.to.data, send_email_form.body.data)
    #Nje konfirmim dhe render_template
    return render_template('loggedin.html', EmailForm=send_email_form)

  return render_template('signin.html', form=sign_in_form)

if __name__ == '__main__':
  app.run(debug=True)
