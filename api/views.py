from flask import Blueprint, jsonify, request
from . import db
from .models import Article
from .loadDataTest import trainModel,testArticle
# from loadDataTest import 
from . import db 

main = Blueprint('main', __name__)

#we do a post request on this (can only accept posts)
@main.route('/add_article', methods = ['POST'])

def add_article():
    #get json
    article_url = request.get_json()
    #update article_data to include stuff from our model like sentiment
    article_data = article_url #for now
    mytitle = "FAKE-TITLE"
    new_article = Article(title = mytitle, sentiment=article_data['sentiment'])
    db.session.add(new_article)
    db.session.commit()

    return 'DONE', 201

#we do a get request on this
@main.route('/display_accuracy')
def display_accuracy():
    #integrate model here
    result,vectorizer,classifier = trainModel()
    
    return 'DONE', 201