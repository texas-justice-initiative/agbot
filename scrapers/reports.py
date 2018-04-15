from datetime import date, datetime, timedelta
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import re
import smtplib

import requests


class Reports:
    def __init__(self, email_settings):
        self.email_from = email_settings['from']
        self.email_to = email_settings['to']
        self.gmail_password = email_settings['gmail_password']

    def scrape(self):
        url = 'https://www.texasattorneygeneral.gov/cj/peace-officer-involved-shooting-report'
        poid_type = {
            'pattern': re.compile('ReportPOIDListCtrl.*scope\.reportsAll = (\[.*2015-0000102.pdf\'})',
                                  re.MULTILINE | re.DOTALL),
            'subject': 'agofficebot: New Release: Peace Officer Involved Injuries or Death',
        }
        oid_type = {
            'pattern': re.compile('ReportOIDListCtrl.*scope\.reportsAll = (\[.*2015-0000001.pdf\'})',
                                  re.MULTILINE | re.DOTALL),
            'subject': 'agofficebot: New Release: Injuries or Death of Peace Officer',
        }

        r = requests.get(url)
        if r.status_code == 200:
            contents = r.text
        else:
            print(f'Failed to download from {url}')
            r.raise_for_status()

        for report_type in [poid_type, oid_type]:
            try:
                files = self.pull_reports_metadata(report_type['pattern'], contents)
            except Exception:
                print('Failed to load the files json array')
                raise

            for entry in files:
                publish_date = datetime.strptime(entry['edor_date'], '%Y-%m-%d').date()
                if publish_date == date.today() - timedelta(1):
                    r = requests.get(entry['file'])

                    if r.status_code == 200:
                        attachment = {
                            'name': entry['file'].split('/')[-1],
                            'content': r.text,
                        }
                    else:
                        print('Failed to download the attachment:', entry['file'])

                    text = f'''
                    Agency: {entry['agency']}
                    Report Date: {entry['dor']}
                    Release Date: {entry['edor_date']}
                    File: {entry['file']}
                    '''

                    self.send_email(subject=report_type['subject'], text=text, attachment=attachment)

    # noinspection PyMethodMayBeStatic
    def pull_reports_metadata(self, pattern, contents):
        match = pattern.search(contents)
        json_content = match.group(1) + ']'
        json_content = json_content.replace("'", '"').replace('\\\\"', "'")
        return json.loads(json_content)

    def send_email(self, subject, text, attachment):
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
            smtp.sendmail(self.email_from, send_to, msg.as_string())
            smtp.close()
        except Exception:
            print(f'Failed to send the email')
            raise
