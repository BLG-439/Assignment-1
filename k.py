# import speech_recognition as sr

# r1 = sr.Recognizer()


# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

# with sr.Microphone() as source:
#     r1.adjust_for_ambient_noise(source)
#     audio = r1.listen(source)
#     get = r1.recognize_google(audio)
#     print(get)

from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import email
import imaplib
import smtplib #Defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon
import smtplib, ssl
import getpass
from bs4 import BeautifulSoup

# tts = gTTS('Hello! Welcome to our application.')
# tts.save('hello.mp3')
#
# tts = gTTS('To sign in, please say your email.')
# tts.save('sign_in1.mp3')
#
# tts = gTTS('Please, say your password.')
# tts.save('sign_in2.mp3')
#
# tts = gTTS('The email does not exist. Please say your email again.')
# tts.save('email_sign_in_error.mp3')
#
# tts = gTTS('The password is incorrect! Please say the password again.')
# tts.save('password_sign_in_error.mp3')
#
# tts = gTTS('Signed in successfully.')
# tts.save('success.mp3')
#



#get voice versions of these and turn them to text
#hotmail does not work
# sender_email = "shqiperi124@hotmail.com"
# receiver_email = "shqiperi124@hotmail.com"


# password = getpass.getpass("Type your password and press enter: ")
def send_email(sender_email, password, receiver_email, message):
  port = 465  # For SSL


  # Create a secure SSL context
  context = ssl.create_default_context()
  server=smtplib.SMTP_SSL("smtp.gmail.com", port)
  # In case of outlook server = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
  server.login(sender_email, password)
  server.sendmail(sender_email, receiver_email, message)
  server.quit()

#def read_inbox(sender_email, password):
#
#      automated_msg=[]
#      #instead of this get password in voice and turn it to text
#
#
#      mail=imaplib.IMAP4_SSL("imap.gmail.com")
#      mail.login(sender_email, password)
#      mail.select('inbox')
#      typ,data = mail.search(None, '(UNSEEN)')
#      mail_ids = data[0]
#
#
#      if(not mail_ids):
#        automated_msg.append('No emails unread')
#      else:
#
#        id_list = mail_ids.split()
#
#        for id_ in reversed(id_list):
#          header_type, header_data = mail.fetch(id_, '(RFC822)' )
##          body_type, body_data = mail.fetch(id_, '(UID BODY[TEXT])')
#
#          for header_response_part, body_response_part in zip(header_data, body_data):
#            if isinstance(header_response_part,tuple) and isinstance(body_response_part,tuple):
#              header_msg = email.message_from_string(header_response_part[1])
#              from_= 'From : ' + header_msg['from'] + '\n'
#              subject_= 'Subject : ' + header_msg['subject'] + '\n'
#              body_msg=body_response_part[1]
#              soup = BeautifulSoup(body_msg, "html.parser")
#              body = 'Body : ' + soup.get_text()
#              automated_msg.append(from_ + subject_ + body)
#      mail.logout()
#      return automated_msg

def get_from_subject_body(header_response_part, body_response_part):

    header_msg = email.message_from_string(header_response_part)
    body_msg = email.message_from_string(body_response_part)
    from_ = header_msg['from']
    subject_ = header_msg['subject']
    body_msg=body_response_part
    soup = BeautifulSoup(body_msg, "html.parser")
    body = soup.get_text()
    return from_, subject_, body

def read_inbox(from_, subject_, body):

    automated_msg = ('From : ' + from_ +
                     '\nSubject : ' + subject_ +
                     '\nBody : '  + body)
    return automated_msg

def go_over_inbox(sender_email, password):
      mail=imaplib.IMAP4_SSL("imap.gmail.com")
      mail.login(sender_email, "weliveinasociety")
      mail.select('inbox')
      typ,data = mail.search(None, '(UNSEEN)')
      mail_ids = data[0]
      print(mail_ids)


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
            #forward_message=forward_msg(from_,receiver_email,subject_,body)
            #send_email(receiver_email,forward_message)

            return read_inbox(from_, subject_, body)

#send_email(receiver_email, message)
def get_messages(sender_email, password):
  Messages=[]
  hold=go_over_inbox(sender_email, password)
  while(hold):
    Messages.append(hold)
    hold=go_over_inbox(sender_email, password)
  return Messages

#get_messages("arthurfleck40@gmail.com", "weliveinasociety")
#for i in msgs:
#  print i
messages=get_messages("arthurfleck40@gmail.com", "weliveinasociety")
i=0
for message in messages:
  print(message)
  i+=1
  tts = gTTS(message)
  tts.save('kot'+str(i)+'.mp3')
