import smtplib
from smtplib import SMTP,SMTPAuthenticationError,SMTPException


host="smtp.gmail.com"
port=587
username="youremail@gmail.com"
password="password"
from_email=username
to_list=["youremail@gmail.com"] #list of emailaddresses you want to mail to 

email_conn=SMTP(host,port)
email_conn.ehlo()
email_conn.starttls()
try:
	email_conn.login(username,"password")
	email_conn.sendmail(from_email,to_list,"CAN ANYBODY HEAR ME")
except smtplibSMTPAuthenticationError:
	print("Login failed")
except:
	print("An error occured")

email_conn.quit()