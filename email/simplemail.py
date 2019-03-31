import smtplib
import config

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login(config.fromaddr,config.password)

msg = "test"

server.sendmail(config.fromaddr, config.toaddr, msg)

server.quit
