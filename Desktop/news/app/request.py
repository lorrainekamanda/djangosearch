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

def process_results(news_list):

    """
    this function uses the get method to get data from the server
    """

    news_results = []

    for entry in news_list:
        id = entry.get('id')
        source = entry.get('source')
        name =entry.get('name')
        author = entry.get('author')
        title = entry.get('title')
        description = entry.get('description')
        url = entry.get('url') 
        urlToImage = entry.get ('urlToImage')
        publishedAt = entry.get ('publishedAt')
        content = entry.get('content') 

        if content:
            news_object = News(author,source,title,description,url,urlToImage,publishedAt,content)
            news_results.append(news_object)
        elif name:
            source_object = Source(id,name)
            news_results.append(source_object)
    


    return news_results



