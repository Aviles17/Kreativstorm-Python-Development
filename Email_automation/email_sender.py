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
import os
import json
import schedule
import time
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from credentials import email, password


#Create function to send an email
def send_email(email: dict, origin_email: str, password: str):
    message = MIMEMultipart()
    message['Subject'] = email['subject']
    message['From'] = origin_email
    message['To'] = ", ".join(email['to'])
    message.attach( MIMEText(email['body']))
    if email['attachments']:
        message = manage_attachments(message, email['attachments'])
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        try:
            smtp_server.login(origin_email, password)
            smtp_server.sendmail(message['From'], email['to'], message.as_string())
        except Exception as e:
            logging.error(f'Error sending the email: {e}')
            print(f'Error sending the email: {e}')
            return False
    return True


#Create function to read email from directory
def read_files_from_dir(path_dir: str):
    to_send_files = []
    if os.path.isdir(path_dir):
        files = os.listdir(path_dir)
        for file in files:
            if os.path.isfile(os.path.join(path_dir, file)):
                with open(os.path.join(path_dir, file), "r") as json_file:
                    data = json.load(json_file)
                    to_send_files.append(data)
            else:
                raise FileNotFoundError(f'File {file} is not a file')
    else:
        raise FileExistsError(f'Directory {path_dir} does not exist')
    
    return to_send_files


#Create function to manage attachments
def manage_attachments(message: MIMEMultipart, attachments: list):
    for file_path in attachments:
            try:
                part = MIMEBase('application', 'octet-stream')
                with open(file_path, 'rb') as file:
                    part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename= {os.path.basename(file_path)}')
                message.attach(part)
            except Exception as e:
                logging.error(f'Error al adjuntar el archivo {file_path}')
                return False
            
    return message

def main_flux(PATH: str):
    emails = read_files_from_dir(PATH)
    for message in emails:
        ret = send_email(message, email, password)
        if ret:
            logging.info("Message succesfully sent")
        else:
            logging.error("Error sending message")



if __name__ == "__main__":
    # Configure the logging module
    logging.basicConfig(filename='email_sender.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
    
    PATH = "Resources\\mock_mails" # Constant Path to read emails from
    
    #Create object to run script daily at 8:00
    schedule.every().day.at("08:00").do(lambda: main_flux(PATH))
    
    while True:
        schedule.run_pending()
        time.sleep(1)