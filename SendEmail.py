import smtplib
from CreateEmailContent import message

# List of To addresses to which the email must be sent.
to_address = ["XXXX@gmail.com"]

# Create a SMTP session
mail_server = smtplib.SMTP_SSL('smtp.gmail.com')

# Login into the initialized mail server using the email id and password.
mail_server.login("<Email ID>", '<Password>')
mail_server.set_debuglevel(1)

# Loop over the email addresses and send the email.
for mail_id in to_address:
    message['To'] = mail_id
    mail_server.send_message(message)
    del message['To']
mail_server.quit()
