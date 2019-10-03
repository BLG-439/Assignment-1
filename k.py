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
# tts = gTTS('To send a new mail say "SEND AN EMAIL". To check the inbox say "CHECK INBOX". To log out say "LOG OUT". To hear the menu again say "HEAR MENU".')
# tts.save('main_menu.mp3')

sound = AudioSegment.from_file("hello.mp3", format="mp3")
play(sound)

sound = AudioSegment.from_file("sign_in1.mp3", format="mp3")
play(sound)
sender_email = "shqiperi124@gmail.com"
kot="ajt"
kot=raw_input("a")

sound = AudioSegment.from_file("sign_in2.mp3", format="mp3")
play(sound)
receiver_email = "shqiperi124@gmail.com"
kot=raw_input("a")



sound = AudioSegment.from_file("sign_in1.mp3", format="mp3")
play(sound)
message = """\
Subject: Hi there

234567io"""
kot=raw_input("a")



#get voice versions of these and turn them to text
#hotmail does not work
# sender_email = "shqiperi124@hotmail.com"
# receiver_email = "shqiperi124@hotmail.com"




# password = getpass.getpass("Type your password and press enter: ")
def send_email(receiver_email, message):

  port = 465  # For SSL


  # Create a secure SSL context
  context = ssl.create_default_context()
  server=smtplib.SMTP_SSL("smtp.gmail.com", port)
  # In case of outlook server = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
  server.login(sender_email, "KotKotKot")
  server.sendmail(sender_email, receiver_email, message)
  server.quit()


def read_inbox():

      automated_msg=[]
      #instead of this get password in voice and turn it to text


      mail=imaplib.IMAP4_SSL("imap.gmail.com")
      mail.login(sender_email, "KotKotKot")
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
