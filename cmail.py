# password:  'kyxs boxq mvsz tlvg'
import smtplib
from email.message import EmailMessage
def send_mail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('januharika96@gmail.com','kyxs boxq mvsz tlvg')
    msg=EmailMessage()
    msg['FROM']='januharika96@gmail.com'
    msg['TO']=to
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg)
    print('Message Sent Successfully')
    server.close()
