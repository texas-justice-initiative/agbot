from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


class Email:
    def __init__(self, settings):
        self.email_from = settings['from']
        self.email_to = settings['to']
        self.gmail_password = settings['gmail_password']

    def send(self, subject, text, attachment):
        send_to = ','.join(self.email_to)

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self.email_from
        msg['To'] = send_to
        msg.preamble = subject

        msg.attach(MIMEText(text))

        msg.attach(MIMEApplication(
            attachment['content'],
            Content_Disposition=f'attachment; filename="{attachment["name"]}"',
            Name=attachment['name']
        ))

        try:
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.ehlo()
            smtp.starttls()
            smtp.login(self.email_from, self.gmail_password)
            smtp.sendmail(self.email_from, self.email_to, msg.as_string())
            smtp.close()
        except Exception:
            print(f'Failed to send the email for:\n{text}')
            raise
