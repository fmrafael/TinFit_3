from flask import Flask, render_template
from api_google_tin import *
from api_news import *
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
 


if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8080, debug=True)
