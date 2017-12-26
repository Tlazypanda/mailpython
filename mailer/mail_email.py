import smtplib
from smtplib import SMTP,SMTPAuthenticationError,SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


host="smtp.gmail.com"
port=587
username="youremail@gmail.com"
password="password"
from_email=username
to_list=["youremail@gmail.com"] #list of emailaddresses you want to mail to 


try:
	email_conn=SMTP(host,port)
	email_conn.ehlo()
	email_conn.starttls()
	email_conn.login(username,"password")
	



	the_msg=MIMEMultipart("alternative")
	the_msg['Subject']="Hello world"
	the_msg['From']=from_email
	the_msg['To']=to_list[0]

	plain_txt="message test"
	html_txt="""\
	<html>
		<head></head>
		<body>
		   <p>hey<br><b>ola amigos</b></p>
		</body>
	</html>
	"""

	part_1=MIMEText(plain_txt,"plain")
	part_2=MIMEText(html_txt,"html")

	the_msg.attach(part_1)
	the_msg.attach(part_2)

	print(the_msg.as_string())

	email_conn.sendmail(from_email,to_list,the_msg.as_string())
	email_conn.quit()
except smtplib.SMTPException:
	print("error sending message")
	