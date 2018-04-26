from scrapers.reports import Reports
from utils.email import Email
import settings


def handle(event, context):
    reports_scraper = Reports()
    email = Email(settings=settings.EMAIL)

    print('Scraping reports')
    reports = reports_scraper.scrape()
    print('Found:', [r['metadata']['file'] for r in reports])

    print('Sending emails to', email.email_to)
    for report in reports:
        subject, text, attachment = prep_email(report)
        email.send(subject, text, attachment)

    print('Done!')


def prep_email(report):
    text = f'''
           Agency: {report['metadata']['agency']}
           Report Date: {report['metadata']['dor']}
           Release Date: {report['metadata']['edor_date']}
           File: {report['metadata']['file']}
           '''

    return report['metadata']['type'], text, report['contents']
