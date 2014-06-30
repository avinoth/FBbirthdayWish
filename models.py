from app import db
from flask.ext.social import Social
from flask.ext.social.datastore import SQLAlchemyConnectionDatastore

app.config['SECURITY_POST_LOGIN'] = '/profile'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.Integer(120))
    lname = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)
    uname = db.Column(db.String(50), unique=True)
    dob = db.Column(db.DateTime)
    country = db.Column(db.String(80))
    friends = db.relationship('Friend', backref = 'friendof', lazy = 'dynamic')


    def __repr__(self):
        return '<User %r>' % (self.name)

class Friend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(120))
    lname = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)
    dob = db.Column(db.DateTime)
    country = db.Column(db.Integer(120))
    lastmessage = db.Column(db.Integer(1500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __repr__(self):
        return '<FriendName %r>' % (self.name)


