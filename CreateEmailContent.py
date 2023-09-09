from email.message import EmailMessage
import mimetypes

#Initialize a emailmessage class.
message = EmailMessage()

#Provide the from address.
message['From'] = "<Email_ID>"

#Provide the Subject of the Email.
message['Subject'] = "Python Developer - Looking for Opportunities"

# Frame a Email body
body = """
Hi,

I hope this email finds you well. My name is **<Name>**, and I am reaching out to express my interest in opportunities within your network for Python Developers. With a background in Python development and a passion for creating innovative solutions, I am eager to explore potential openings through your expertise.

I have **<No of years> years** of experience in Python development, with a strong foundation in **Network Automation**. My proficiency extends to **Microservices development, API Integration.**

What excites me most about the field of Python development is its ever-evolving nature and the potential to work on projects that push the boundaries of innovation. I am committed to staying at the forefront of emerging technologies and thrive on the opportunity to take on new challenges.

I have **attached my resume** to provide you with a comprehensive overview of my qualifications and experiences. I am confident that my skills align well with the needs of Python development roles, and I am enthusiastic about the possibility of collaborating with your clients.

If you have any openings or insights that you believe could be a strong match for my skills, I would greatly appreciate the opportunity to connect and explore potential opportunities further. Please feel free to reach out to me at **<Email ID>** or **<Password>**. I am currently in <Place> and on <VISA Status>.

Thank you for considering my email, and I look forward to the possibility of collaborating with you to explore exciting Python Developer roles.

Regards,
<Name>
https://www.linkedin.com/in/XXXXX/
"""
# The body of the message must be set to message object.
message.set_content(body)

# In order to attach a file, we need to identify the mime_type and mime_subtype of the file.
mime_type, _ = mimetypes.guess_type('Name_Of_the CV.pdf')
mime_type, mime_subtype = mime_type.split("/")

# With this, we add the attachment to the message object.
with open('Name_Of_the CV.pdf', 'rb') as file:
 message.add_attachment(file.read(),
 maintype=mime_type,
 subtype=mime_subtype,
 filename='Name_Of_the CV.pdf')

