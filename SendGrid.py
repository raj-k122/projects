import base64
import os
from sendgrid.helpers.mail import (
    Mail, Attachment, FileContent, FileName,
    FileType)
from sendgrid import SendGridAPIClient

message = Mail(
    from_email='rajkuls2014@gmail.com', #email that sends the message
    to_emails='email.alert.python@gmail.com', #email that receives the message
    subject='Important message from the back office',
    html_content='<strong>look at this file</strong>'
)

# this file passed into the variable document should include the path it is located in. In this case I
#kept the file in my python project folder, hence I simply wrote the file name.
document = 'resume.pdf'
with open(document, 'rb') as f:
    data = f.read()
    f.close()
encrypt = base64.b64encode(data).decode()
at = Attachment()
at.file_content = FileContent(encrypt)
at.file_type = FileType('application/pdf')
at.file_name = FileName('file.pdf')

message.attachment = at

#if using Windows, then define the SENDGRID_API_KEY within the environment variables
#in your OS path.
try:
    grid = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    email = grid.send(message)
    print(email.status_code)
    print(email.body)
    print(email.headers)
except Exception as ex:
    print(ex.message)