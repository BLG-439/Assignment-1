from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import email
import imaplib
import smtplib #Defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon
import smtplib, ssl
import getpass
from bs4 import BeautifulSoup
# import speech_recognition as sr

# r1 = sr.Recognizer()

# with sr.Microphone() as source:
#     r1.adjust_for_ambient_noise(source)
#     audio = r1.listen(source)
#     get = r1.recognize_google(audio)
#     print(get)


#tts = gTTS('Hello! Welcome to our application.')
#tts.save('hello.mp3')
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
kot=input("a")

sound = AudioSegment.from_file("sign_in2.mp3", format="mp3")
play(sound)
password="KotKotKot"
# receiver_email = "shqiperi124@gmail.com"
kot=input("a")

# sound = AudioSegment.from_file("sign_in1.mp3", format="mp3")
# play(sound)
message = """\
Subject: Hi there

234567io"""
# kot=raw_input("a")



#get voice versions of these and turn them to text
#hotmail does not work
# sender_email = "shqiperi124@hotmail.com"
receiver_email = "mateohudhra98@gmail.com"

sender_email_server=(sender_email.split("@")[1]).split(".")[0]

if sender_email_server=="hotmail":
  server = smtplib.SMTP('smtp-mail.outlook.com', 587)

  # mail= DUHET TE SHIKOJM PER "READING" NGA SERVERI I HOTMAILIT
elif sender_email_server=="gmail":
  port = 465  # For SSL

  # Create a secure SSL context
  #For Sending
  # context = ssl.create_default_context()                          ??? PER CA ESHTE KJO SE SIKUR NUK ESHTE PERDORUR NE NDONJE VEND TJETER ???
  server=smtplib.SMTP_SSL("smtp.gmail.com", port)

  # For reading
  mail=imaplib.IMAP4_SSL("imap.gmail.com")
# else other email servers...

server.login(sender_email, password)
mail.login(sender_email, password)

if input("What do you want to do: 1. Send\n2. Read"):
  server.sendmail(sender_email, receiver_email, message)
else:
  #READ
  automated_msg=[]
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
    for i in automated_msg:
      print (i)


# password = getpass.getpass("Type your password and press enter: ")

mail.logout()
server.quit()
