from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")

@app.route('/index')
def index2():  # put application's code here
    return render_template("index.html")

@app.route('/movie')
def movie():  # put application's code here
    datalist = []
    conn = sqlite3.connect("movie.db")
    cur = conn.cursor()
    sql = '''
        select * from movie
    '''
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    return render_template("movie.html", datalist=datalist)

@app.route('/group')
def group():  # put application's code here
    return render_template("group.html")

@app.route('/wordcloud')
def wordcloud():  # put application's code here
    return render_template("wordcloud.html")

@app.route('/rating')
def rating():  # put application's code here
    score = []  # 评分
    num = []  # 评分电影数
    conn = sqlite3.connect("movie.db")
    cur = conn.cursor()
    sql = '''
        select score,count(score) from movie group by score
    '''
    datalist = cur.execute(sql)
    for data in datalist:
        score.append(str(data[0]))
        num.append(data[1])
    cur.close()
    conn.close()

    return render_template("rating.html", score=score, num=num)

if __name__ == '__main__':
    app.run()
