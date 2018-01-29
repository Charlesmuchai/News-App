from app import app
import urllib.request,json
from .models import news

#Getting apiKey
api_key = app.config['NEWS_API_KEY']
News = news.News

#Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]

        def get_news(category):
            get_news_url = base_url.format(category,api_key)
             with urllib.request.urlopen(get_news_url) as url:
                get_news_data = url.read()
                get_news_response = json.loads(get_news_data)

                news_results = None
                if get_news_response['results']:
                    news_results_list = get_news_response['results']
                    news_results = process_results(news_results_list)

    return news_results

        def process_results(news_list):
            news_results = []
            for news_item in news_list:
                id = news_item.get('id')
                author = news_item.get('original_author')
                title = news_item.get('title')
                description = news_item.get('description')
                url = news_item.get('url')
                publishedAt = news_item.get('publishedAt')

    return news_results
