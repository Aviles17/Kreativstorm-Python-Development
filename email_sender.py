''' 
You work at a company that sends daily reports to clients via email. 
The goal of this project is to automate the process of sending these reports via email.

Here are the steps you can take to automate this process:

    Use the smtplib library to connect to the email server and send the emails.

    Use the email library to compose the email, including the recipient's email address, the subject, 
    and the body of the email.

    Use the os library to access the report files that need to be sent.

    Use a for loop to iterate through the list of recipients and send the email and attachment.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the emails that have been sent and any errors 
    that may have occurred during the email sending process. 
'''
import smtplib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



#Create function to send an email
def send_email(email: dict, password: str):
    message = MIMEMultipart()
    message['Subject'] = email['subject']
    message['From'] = email['from']
    message['To'] = email['to']
    message.attach( MIMEText(email['body']))
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 462) as smtp_server:
        try:
            smtp_server.login(email['from'], password)
            smtp_server.sendmail(email['from'], email['to'], message.as_string())
        except Exception as e:
            print(f'Error: {e}')
            return False
        print('Email sent successfully')
    return True

'''
# Adjuntar un archivo al correo (opcional)
attachment_filename = 'reporte.pdf'
with open(attachment_filename, 'rb') as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    part.add_header('Content-Disposition', f'attachment; filename= {attachment_filename}')
    message.attach(part)

# Conectar y enviar el correo
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(message)
    print('Correo enviado correctamente.')

'''