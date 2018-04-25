from scrapers.reports import Reports
from utils.email import Email
import settings


def handle(event, context):
    reports_scraper = Reports()
    email = Email(settings=settings.EMAIL)

    print('Scraping reports')
    reports = reports_scraper.scrape()
    print('Found:', [r['filename'] for r in reports])

    print('Sending emails to', email.email_to)
    for report in reports:
        email.send(report['subject'], report['text'], report['attachment'])

    print('Done!')
