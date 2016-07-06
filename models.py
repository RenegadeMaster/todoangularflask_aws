from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.Text)
    done = db.Column(db.Boolean)
    date = db.Column(db.DateTime)

    def __init__(self, task, done):
        self.task = task
        self.done = done
        self.date = datetime.utcnow()


class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class MeetingStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
