from .request import get_news,search_source
from flask import render_template,request,redirect,url_for
from app import app

@app.route('/')

def index():
    """
    function for getting the news data to dispaly the data on my index.html
    """

    all_news = get_news('totalResults')
   



    print(all_news)

    title = "view News"

    search_news = request.args.get('news_query')

    return render_template('index.html',title = title, totalResults = all_news)




