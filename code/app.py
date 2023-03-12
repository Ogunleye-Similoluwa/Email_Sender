import smtplib
import ssl
from email.message import EmailMessage


email_sender = 'osimiloluwa9@gmail.com'
email_password = 'dlldxlcrmftzozyv'

email_receiver ='simiogunleye18@gmail.com'
subject = "Simex"
body = """
wow
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
