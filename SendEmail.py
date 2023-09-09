import smtplib
from CreateEmailContent import message

to_address = ["XXXX@gmail.com"]

mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
mail_server.login("<Email ID>", '<Password>')
mail_server.set_debuglevel(1)

for mail_id in to_address:
    message['To'] = mail_id
    mail_server.send_message(message)
    del message['To']
mail_server.quit()
