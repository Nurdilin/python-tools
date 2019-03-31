import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config
import email.utils


msg = MIMEMultipart()
msg['Subject'] = "Sub Example"
msg['To'] = email.utils.formataddr(('Recipient', config.toaddr))
msg['From'] = email.utils.formataddr(('Author', config.fromaddr))

body = "example message"
msgBody = MIMEText(body, 'plain')
msg.attach(msgBody)


# simplemail.py code here:
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, config.password)
text = msg.as_string()
print "Text is:", text
server.sendmail(fromaddr, toaddr, text)
server.quit()
