import email
import imaplib
import smtplib
import smtplib, ssl
import getpass
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
import textwrap
#get voice versions of these and turn them to text
sender_email = "isallari.megi@gmail.com"
receiver_email = "isallari.megi@gmail.com"
message = """\
Subject: Hi there

Elvis Presley- Devil in disguise"""
 #instead of this get password in voice and turn it to text
password = getpass.getpass("Type your password and press enter: ")

def send_email(receiver_email, message):

  port = 465  # For SSL


  # Create a secure SSL context
  context = ssl.create_default_context()
  server=smtplib.SMTP_SSL("smtp.gmail.com", port)
  server.login(sender_email, password)
  server.sendmail(sender_email, receiver_email, message)
  server.quit()

def get_from_subject_body(header_response_part, body_response_part):

    header_msg = email.message_from_string(header_response_part)
    body_msg = email.message_from_string(body_response_part)
    from_ = header_msg['from']
    subject_ = header_msg['subject']
    body_msg=body_response_part
    soup = BeautifulSoup(body_msg, "html.parser")
    body = soup.get_text()
    return from_, subject_, body

def forward_msg(from_,to_,subject_, body):
    intro='--------Forwarded message-------- \n\n\n'

    intro_from='From: '+from_+'\n'
    intro_to='To: '+to_+'\n'
    intro_subject='Subject: '+ subject_+'\n\n\n'
    body = intro+intro_from+intro_to+intro_subject+body

    msg = MIMEText(body)
    msg['Subject'] = 'Fwd: ' + subject_
    msg['To'] = to_
    return msg.as_string()

def read_inbox(from_, subject_, body):

    automated_msg = ('From : ' + from_ + '\n' +
                     'Subject : ' + subject_ + '\n' +
                     'Body : '  + body)
    return automated_msg

def go_over_inbox():


      mail=imaplib.IMAP4_SSL("imap.gmail.com")
      mail.login(sender_email, password)
      mail.select('inbox')
      typ,data = mail.search(None, '(UNSEEN)')
      mail_ids = data[0]


      if(not mail_ids):
          print ('No emails unread')
          return
      else:

        id_list = mail_ids.split()

        for id_ in reversed(id_list):
          header_type, header_data = mail.fetch(id_, '(RFC822)' )
          body_type, body_data = mail.fetch(id_, '(UID BODY[TEXT])')

          if isinstance(header_data[0],tuple) and isinstance(body_data[0],tuple):
            header_response_part = header_data[0][1].decode('utf-8')
            body_response_part= body_data[0][1].decode('utf-8')
            from_,subject_,body = get_from_subject_body(header_response_part ,body_response_part)
            #READ INBOX
            print (read_inbox(from_,subject_,body))
            #FORWARD MESSAGE
            forward_message=forward_msg(from_,receiver_email,subject_,body)
            send_email(receiver_email,forward_message)

            return

send_email(receiver_email, message)
go_over_inbox()
