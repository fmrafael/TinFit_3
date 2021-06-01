import os 
from newsapi import NewsApiClient
from datetime import date,datetime,timedelta

today = datetime.utcnow()
days_delta = timedelta(10)
thirty_days_ago = today - days_delta

API_KEY_NEWS = os.environ['API_KEY_NEWS']

newsapi = NewsApiClient(api_key=API_KEY_NEWS)

data = newsapi.get_sources(country='br')["sources"]

data_source = []
for i in data:
  data_source.append(i['id'])

id = ', '.join(data_source)
 
all_articles = newsapi.get_everything(q='futebol',
                                      sources = id,
                                      from_param=thirty_days_ago,
                                      to=today,
                                      page=2)['articles']


title_news = [article['title'].title() for article in all_articles]
desc_news = [article['description'] for article in all_articles]
url_news = [article['url'] for article in all_articles]
urlToImage_news = [article['urlToImage'] for article in all_articles]
source_news = [article['source']['name'] for article in all_articles]


title_news.reverse()
desc_news.reverse()
url_news.reverse()
urlToImage_news.reverse()
source_news.reverse()