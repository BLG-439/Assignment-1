import email
import imaplib
import smtplib
import smtplib, ssl
import getpass
from bs4 import BeautifulSoup

#get voice versions of these and turn them to text
sender_email = "isallari.megi@gmail.com"
receiver_email = "isallari.megi@gmail.com"
message = """\
Subject: Hi there

Elvis Presley- Devil in disguise"""
password = getpass.getpass("Type your password and press enter: ")
def send_email(receiver_email, message):

  port = 465  # For SSL


  # Create a secure SSL context
  context = ssl.create_default_context()
  server=smtplib.SMTP_SSL("smtp.gmail.com", port)
  server.login(sender_email, password)
  server.sendmail(sender_email, receiver_email, message)
  server.quit()


def read_inbox():

      automated_msg=[]
      #instead of this get password in voice and turn it to text


      mail=imaplib.IMAP4_SSL("imap.gmail.com")
      mail.login(sender_email, password)
      mail.select('inbox')
      typ,data = mail.search(None, '(UNSEEN)')
      mail_ids = data[0]


      if(not mail_ids):
        automated_msg.append('No emails unread')

      else:

        id_list = mail_ids.split()

        for id_ in reversed(id_list):
          header_type, header_data = mail.fetch(id_, '(RFC822)' )
          body_type, body_data = mail.fetch(id_, '(UID BODY[TEXT])')

          for header_response_part, body_response_part in zip(header_data, body_data):
            if isinstance(header_response_part,tuple) and isinstance(body_response_part,tuple):
              header_msg = email.message_from_string(header_response_part[1])
              from_= 'From : ' + header_msg['from'] + '\n'
              subject_= 'Subject : ' + header_msg['subject'] + '\n'
              body_msg=body_response_part[1]
              soup = BeautifulSoup(body_msg, "html.parser")
              body = 'Body : ' + soup.get_text()
              automated_msg.append(from_ + subject_ + body)

      return automated_msg

send_email(receiver_email, message)
msgs=read_inbox()
for i in msgs:
  print i
  
