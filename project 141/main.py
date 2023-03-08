from flask import Flask,request,jsonify
import csv

all_articles = []
liked_articles = []
not_liked_articles = []

with open("articles.csv") as f:
    data1 = csv.reader(f)
    data = list(data1)
    all_articles = data[1:]

@app.route("/get_article")
def get_article():
    return jsonify({
        "data": all_articles[0],
        "status":"success"
    })

@app.route("/liked_articles", methods=['POST'])
def liked_articles():
    global all_articles
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
       "status":"success" 
    }),201

@app.route("/disliked_articles", methods=['POST'])
def disliked_articles():
    global all_articles
    article = all_articles[0]
    disliked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
       "status":"success" 
    }),201


app = Flask(__name__)

if __name__ == "__main__":
    app.run()