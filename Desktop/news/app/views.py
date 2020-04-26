from .request import get_news,search_source,get_new
from flask import render_template,request,redirect,url_for
from app import app

@app.route('/')

def index():
    """
    function for getting data from request and dispaly on index.html
    """

    all_news = get_news('totalResults')
   
    print(all_news)

    title = "view News"

    search_news = request.args.get('news_query')

    if search_news:
          return redirect(url_for('search', source_name = search_news  ))
    else:
          return render_template('index.html',title = title, totalResults = all_news)




@app.route('/search<source_name>')

def search(source_name):
    search_source_list = source_name.split(" ")
    source_name_format =  "+".join(search_source_list)
    searched_source = search_source(source_name_format)
    title = f'results for {source_name}'
    return render_template('search.html', news = searched_source)

