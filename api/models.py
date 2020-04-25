from . import db

class Article(db.Model):
    # url = db.Column(db.String, primary_key = True)
    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    sentiment = db.Column(db.String)