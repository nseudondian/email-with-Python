from email.message import EmailMessage
from priv import password
import ssl
import smtplib

email_sender = "nseabasiudondian@gmail.com"
email_password = password

email_receiver = 'perela4979@etondy.com'

subject = "Promo Announcement"
body = """ Courses will sell a lot cheaper from March 31"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


