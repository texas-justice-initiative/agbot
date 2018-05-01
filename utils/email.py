from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


class Email:
    def __init__(self, settings):
        self.email_from = settings['from']
        self.email_to = settings['to']

        self.account_password = settings['account_password']
        self.server_address = settings['server_address']
        self.server_port = settings['server_port']

    def send(self, subject, text, attachment):
        """
        Sends an email.

        :param subject: Subject line of the email
        :param text: Body of the message
        :param attachment: A binary of the contents of the attachment
        """
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
            smtp = smtplib.SMTP(self.server_address, self.server_port)
            smtp.ehlo()
            smtp.starttls()
            smtp.login(self.email_from, self.account_password)
            smtp.sendmail(self.email_from, self.email_to, msg.as_string())
            smtp.close()
        except Exception:
            print(f'Failed to send the email for:\n{text}')
            raise
