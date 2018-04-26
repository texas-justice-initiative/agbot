from datetime import date, datetime, timedelta
import json
import re

import requests


class Reports:
    def __init__(self):
        pass

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

        reports = []
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

                    entry['type'] = report_type['subject']
                    reports.append({
                        'metadata': entry,
                        'contents': attachment,
                    })
        return reports

    # noinspection PyMethodMayBeStatic
    def pull_reports_metadata(self, pattern, contents):
        match = pattern.search(contents)
        json_content = match.group(1) + ']'
        json_content = json_content.replace("'", '"').replace('\\\\"', "'")
        return json.loads(json_content)
