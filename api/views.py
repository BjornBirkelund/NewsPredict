from flask import Blueprint, jsonify, request
from . import db
from .models import Article,jsonData
from .loadData import testArticle

main = Blueprint('main', __name__)
#train the model when the user visits the site before anything else is done.


@main.route('/testUrl', methods = ['POST'])
def display_accuracy():
    link = request.get_json(force=True)
    title, prediction = testArticle(link['url'])
    output = "Title: "+title +"\nPrediction: "+ prediction
    return output, 201 