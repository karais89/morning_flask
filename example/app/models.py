from flask import current_app
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username


class UserGameCenterStage(db.Model):
    sno = db.Column(db.String(80), primary_key=True)
    version = db.Column(db.Integer, primary_key=True)
    stageIndex = db.Column(db.Integer, primary_key=True)
    bestScore = db.Column(db.Integer, nullable=False)