from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer(120), unique=True)
    email = db.Column(db.Integer(120), unique=True)
    configkey = db.Column(db.Integer(200), unique=True)
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
