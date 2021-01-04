import scrapy, json, datetime, time
from datetime import timedelta, date

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

class Covid19Spider(scrapy.Spider):
    name = 'covid19'
    allowed_domains = ['covid-193.p.rapidapi.com']
    # start_urls = ['https://covid-193.p.rapidapi.com/statistics']

    # start_date = date.today() - timedelta(days=60)
    start_date = date(2020, 3, 22)
    end_date = date.today()

    start_urls = ['https://covid-193.p.rapidapi.com/history?country=indonesia&day='+str(date) for date in daterange(start_date, end_date)]
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'data_idn.csv'
    }

    def parse(self, response):
        resp = json.loads(response.body).get('response')
        filter = [resp[0]]

        for data in filter:
            yield {
                'country': data.get('country'),
                'total': data.get('cases').get('total'),
                'active': data.get('cases').get('active'),
                'recovered': data.get('cases').get('recovered'),
                'new_cases': data.get('cases').get('new'),
                'new_deaths': data.get('deaths').get('new'),
                'total_deaths': data.get('deaths').get('total'),
                'total_tests': data.get('tests').get('total'),
                'date': data.get('day'),
                'latest_update': data.get('time')
            }
            time.sleep(2)
 
