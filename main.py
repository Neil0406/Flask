from flask import Flask, render_template
from datetime import datetime
from weather import weather
from taiwan_bank import tb
from news import news

app = Flask(__name__)

def dtime():
    return datetime.today().strftime('%Y-%m-%d')

@app.route("/")
def index():

    return render_template("index.html" , today = dtime(),data = weather()[0]['臺北市'], data1 = weather()[1]['臺北市']
        , data2 = weather()[2]['臺北市'], usd = tb()[0], jpy = tb()[7], aud = tb()[3], eur = tb()[14], news = news()

    )


# @app.route("/about")
# def about():
#     return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)


#render_template將會找尋html檔案傳送給使用者
#前往 http://localhost:5000/

