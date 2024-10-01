# masoneweernesto@gmail.com #Desde donde se manda el correo
# onewemas2323@gmail.com

# Vamos a esta pagina para coger nuestra clave
# https://myaccount.google.com/u/0/apppasswords?pli=1&rapt=AEjHL4PwNTwHJlakRhpvyQPEa5N7srEggbsAocHxaxKRku4tbGQ7JrS8lFeV5GVOiC0cBqvTFLT6afGNdI4A5MMqe7Na-XUbzVwq45TIoJp8BcZWijDRJis
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

your_email = 'masoneweernesto@gmail.com'
your_password = 'agfc kset wdll skbl'

recipent = 'onewemas2323@gmail.com'

message = MIMEMultipart()
message['From'] = your_email
message['To'] = recipent
message['Subject'] = 'Email de agradecimiento'

body = 'Muchas gracias a todos por el apoyo!! Se agradece mucho <3'
message.attach(MIMEText(body, 'plain'))

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()
smtp_server.login(your_email, your_password)

smtp_server.sendmail(your_email, recipent, message.as_string())
smtp_server.quit()
print("Email enviado")
