import unittest
from email.mime.multipart import MIMEMultipart
from email_sender import manage_attachments, send_email, read_files_from_dir
from credentials import email, password

class TestEmailSender(unittest.TestCase):
    
    def test_credentials(self):
        self.assertIsInstance(email, str, "Email should be a string")
        self.assertNotEqual(email, "", "Email should not be empty.")
        self.assertIsInstance(password, str, "Password should be a string")
        self.assertNotEqual(password, "", "Password should not be empty.")

    def test_manage_attachments(self):
        message = MIMEMultipart()
        attachments = ['Resources\\mock_attachments\\Lorem_Ipsum_1.pdf', 'Resources\\mock_attachments\\Lorem_Ipsum_2.pdf']  # Asegúrate de tener este archivo en tu directorio
        result = manage_attachments(message, attachments)
        self.assertIsInstance(result, MIMEMultipart, "The result should be a MIMEMultipart object")

    def test_send_email_no_attachment(self):
        message = MIMEMultipart()
        message['From'] = email
        message['To'] = 'test@example.com'
        message['Subject'] = 'Test'
        message['body'] = "Test email body"
        
        result = send_email(message, email, password)
        self.assertEqual(result, True, "The result should be True if the email was sent successfully")

    def test_send_email_attachments(self):
        message = MIMEMultipart()
        message['from'] = email
        message['to'] = 'test@example.com'
        message['subject'] = 'Test'
        message['body'] = "Test email body"
        message['attachments'] = ['Resources\\mock_attachments\\Lorem_Ipsum_1.pdf', 'Resources\\mock_attachments\\Lorem_Ipsum_2.pdf']  # Asegúrate de tener este archivo en tu directorio
        
        result = send_email(message, email, password)
        self.assertEqual(result, True, "The result should be True if the email was sent successfully")
        
    def test_send_email_multiple_recipients(self):
        #recipientslist = ["test@example.com", "test_1@example.com"]
        recipientslist = ["santiaviles17@gmail.com", "unimedpuebas@gmail.com"]
        message = MIMEMultipart()
        message['From'] = email
        message['To'] = ", ".join(recipientslist)
        message['Subject'] = 'Test'
        message['body'] = "Test email body"
        
        result = send_email(message, email, password)
        self.assertEqual(result, True, "The result should be True if the email was sent successfully")
        
    def test_read_files_from_dir(self):
        path = 'Resources\\mock_mails' 
        result = read_files_from_dir(path)
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    unittest.main()