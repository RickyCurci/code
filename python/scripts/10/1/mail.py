#!/usr/bin/python3
from de_crypting import txt
import smtplib

gmail_user = 'curci.richi@gmail.com'
gmail_password = '127cinque20051RiccardoCurci20051'

sent_from = gmail_user
to = [gmail_user, gmail_user]
subject = 'OMG Super Important Message'

email_text = msg = "\r\n".join([
  "From: user_me@gmail.com",
  "To: user_you@gmail.com",
  subject,
  "",
  str(txt.crypting(2, 'source.txt'))
  ])

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except:
    print('Something went wrong...')
