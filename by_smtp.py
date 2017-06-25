'''This module sends email message asking adreesses, subject and text message from user.
Smtp connection is configured to smtp.mail.ru. So, you should use mail.ru account.
'''

import smtplib
from email.mime.text import MIMEText

print('Hi! It will be cool if you use mail.ru account. Otherwise it will not work.\n')
subject = input('Type subject of message: ')
my_adr = input('Type \'From\' address: ')  # sender's email address
passw = input('Type your email password (it will not be stolen): ')
to_adr = input('Type \'To\' address: ')  # recipient's email address
msg = MIMEText(input('Type your message: '))  # creating Message object with text of the message

msg['Subject'] = subject
msg['From'] = my_adr
msg['To'] = to_adr

s = smtplib.SMTP('smtp.mail.ru', 587)  # connecting to smtp-server
s.ehlo()  # identify ourselves to an smtp server
s.starttls()  # starting encryption
s.ehlo()
s.login(my_adr, passw)

s.send_message(msg)
s.quit()

print('\nThe message has been sent. Have a nice day!')
