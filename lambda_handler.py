from scrapers.reports import Reports
from utils.email import Email
import settings


def handle(event, context):
    reports_scraper = Reports()
    email = Email(settings=settings.EMAIL)

    reports = reports_scraper.scrape()

    for report in reports:
        email.send(report['subject'], report['text'], report['attachment'])

    print('Done!')
