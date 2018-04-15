from scrapers.reports import Reports
import settings


def handle(event, context):
    reports = Reports(email_settings=settings.EMAIL)
    reports.scrape()

    print('Done!')
