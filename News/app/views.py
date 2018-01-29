from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/news/<news_id>')
def news(news_id):

    '''
    View root function that returns the index page and its data
    '''
    message = 'Hello World'
    return render_template('news.html',id = news_id)

@app.route('/')
def index():

    latest_news = get_news('latest')
    print(latest_news)
    title = 'Welcome to The Best News Page Online'
    return render_template('index.html',title = title,latest = latest_news)
