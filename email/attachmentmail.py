import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config
import email.utils
#for attachments : 
from email.mime.base import MIMEBase
from email import encoders

msg = MIMEMultipart()
msg['Subject'] = "Sub Example"
msg['To'] = email.utils.formataddr(('Recipient', config.toaddr))
msg['From'] = email.utils.formataddr(('Author', config.fromaddr))

body = "example message"
msgBody = MIMEText(body, 'plain')
msg.attach(msgBody)



#attachement part:

filename = "attachment.txt"
attachment = open(filename, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment;filename= %s" % filename)
msg.attach(part)



# simplemail.py code here:
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, config.password)
text = msg.as_string()
print "Text is:", text
server.sendmail(fromaddr, toaddr, text)
server.quit()
