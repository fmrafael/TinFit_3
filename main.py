from flask import Flask, render_template
from api_google_tin import *
from api_news import *
from api_stats import *
app = Flask(__name__)



@app.route('/')

def home():
  return render_template("index.html", title_videoId_imageVideo = zip(title,videoId,imageVideo))

@ app.route('/news')
def news():
  return render_template("news.html", news_data = zip(title_news,desc_news,url_news,urlToImage_news,source_news))


@app.route('/about')  

def about():
  return render_template("about.html")

@app.route('/contact')  

def contact():
  return render_template("contact.html")

@app.route('/stats')

def stats():
  return render_template("stats.html", stats_data = zip
  ( round_date,round_name_home,round_logo_home,round_name_away,round_logo_away))
 


if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8080, debug=True)
