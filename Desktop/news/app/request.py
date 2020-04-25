from app import app
import urllib.request,json
from .models import news

News = news.News
Source = news.Source


api_key = '607f7c54f932479fba6a4b8390978690'

base_url = app.config["NEWS_API_BASE_URL"]

def get_news(category):

    """
    function requests the data from the news server
    """

    call_url = base_url.format(category,api_key)

    with urllib.request.urlopen(call_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None
        if get_news_response['articles']:
            results_list = get_news_response['articles']
            news_results = process_results(results_list)
    return news_results


