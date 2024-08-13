import json
from newsapi import NewsApiClient
from datetime import date, timedelta

def source(config):
    client = NewsApiClient(api_key=config['API_KEY'])
    yesterday = str(date.today() - timedelta(days=1))
    yesterday_events = client.get_everything(language="en", from_param=yesterday, sort_by='publishedAt')
    with open('news-'+ yesterday + '.json', 'w') as source_file :
        json.dump(yesterday_events, source_file, indent=2)
