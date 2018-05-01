from scrapers.reports import Reports
from utils.email import Email
import settings


def handle(event, context):
    reports_scraper = Reports()
    email = Email(settings=settings.EMAIL)

    print('Scraping reports')
    reports = reports_scraper.scrape()
    print('Found:', [r['file_url'] for r in reports])

    print('Sending emails to', email.email_to)
    for report in reports:
        subject, text, attachment = prep_email(report)
        email.send(subject, text, attachment)

    print('Done!')


def prep_email(report):
    text = f'''
           Agency: {report['agency']}
           Report Date: {report['report_date']}
           Release Date: {report['release_date']}
           File: {report['file_url']}
           '''

    return report['type'], text, report['contents']


# For local tests
if __name__ == '__main__':
    handle(0, 0)
