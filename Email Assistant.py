pip install imaplib smtplib email-parser
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.parser import BytesParser
from email.policy import default

class EmailAssistant:
    def __init__(self, email, password, smtp_server, imap_server, smtp_port=587, imap_port=993):
        self.email = email
        self.password = password
        self.smtp_server = smtp_server
        self.imap_server = imap_server
        self.smtp_port = smtp_port
        self.imap_port = imap_port

    def send_email(self, to_email, subject, message):
        msg = MIMEText(message)
        msg['From'] = self.email
        msg['To'] = to_email
        msg['Subject'] = subject

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.email, self.password)
            server.sendmail(self.email, to_email, msg.as_string())
        print("Email sent successfully!")

    def read_unread_emails(self):
        with imaplib.IMAP4_SSL(self.imap_server, self.imap_port) as mail:
            mail.login(self.email, self.password)
            mail.select('inbox')
            type, data = mail.search(None, 'UNSEEN')
            mail_ids = data[0].split()
            parser = BytesParser(policy=default)

            for num in mail_ids:
                typ, data = mail.fetch(num, '(RFC822)')
                for response_part in data:
                    if isinstance(response_part, tuple):
                        msg = parser.parsebytes(response_part[1])
                        print('From:', msg['from'])
                        print('Subject:', msg['subject'])
                        print('Body:', msg.get_body(preferencelist=('plain')).get_content())
            mail.logout()
        print("Unread emails listed successfully!")

# Configuration (replace placeholders with your actual details)
email = "your_email@example.com"
password = "your_password"
smtp_server = "smtp.example.com"
imap_server = "imap.example.com"

assistant = EmailAssistant(email, password, smtp_server, imap_server)

# Test sending an email
assistant.send_email("receiver_email@example.com", "Test Subject", "Hello, this is a test email from your AI Email Assistant.")

# Test reading unread emails
assistant.read_unread_emails()
