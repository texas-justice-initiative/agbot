from scrapers.reports import Reports
from utils.datadotworld import Datadotworld
from utils.gsheets import Gsheets
import settings


def handle(event, context):
    reports = Reports(email_settings=settings.EMAIL)
    reports.scrape()

    print('Done!')
