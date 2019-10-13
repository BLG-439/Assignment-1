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


##### SEND #####
#tts = gTTS('Whom would you like to send this email to?')
#tts.save('send_to.mp3')
#tts = gTTS('Say the subject of the email.')
#tts.save('send_subject.mp3')
#tts = gTTS('Say the body of the email.')
#tts.save('send_body.mp3')
#tts = gTTS('There is no email of this category.')
#tts.save('no_email.mp3')
