from app import db
from flask.ext.social import Social
from flask.ext.social.datastore import SQLAlchemyConnectionDatastore

app.config['SECURITY_POST_LOGIN'] = '/profile'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer(120))
    email = db.Column(db.Integer(120), unique=True)
    dob = db.Column(db.DateTime)
    country = db.Column(db.Integer(120))
    friends = db.relationship('Friend', backref = 'friendof', lazy = 'dynamic')


    def __repr__(self):
        return '<User %r>' % (self.name)

class Friend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer(120), unique=True)
    email = db.Column(db.Integer(120))
    dob = db.Column(db.DateTime)
    country = db.Column(db.Integer(120))
    lastmessage = db.Column(db.Integer(1500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __repr__(self):
        return '<FriendName %r>' % (self.name)

class Connection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    provider_id = db.Column(db.String(255))
    provider_user_id = db.Column(db.String(255))
    access_token = db.Column(db.String(255))
    secret = db.Column(db.String(255))
    display_name = db.Column(db.String(255))
    profile_url = db.Column(db.String(512))
    image_url = db.Column(db.String(512))
    rank = db.Column(db.Integer)

Security(app, SQLAlchemyUserDatastore(db, User, Role))
Social(app, SQLAlchemyConnectionDatastore(db, Connection))

