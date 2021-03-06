#----------------------------------------------------------------------------#
# Imports.
#----------------------------------------------------------------------------#

from flask import Flask, redirect, url_for, session, request, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from forms import *
from flask_oauth import OAuth
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
oauth = OAuth()

FACEBOOK_APP_ID = app.config["FACEBOOK_APP_ID"]
FACEBOOK_APP_SECRET = app.config["FACEBOOK_APP_SECRET"]


facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=FACEBOOK_APP_ID,
    consumer_secret=FACEBOOK_APP_SECRET,
    request_token_params={'scope': 'email'}
)


# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''



#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')

def pop_login_session():
    session.pop('logged_in', None)
    session.pop('oauth_token', None)

@app.route('/')
def home():
    return render_template('pages/placeholder.home.html')

@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')

@app.route('/login')
def login():
    return facebook.authorize(callback=url_for('facebook_authorized',
        next=request.args.get('next'), _external=True))


@app.route('/login/authorized')
@facebook.authorized_handler
def facebook_authorized(resp):
    next_url = request.args.get('next') or url_for('profile')
    if resp is None or 'access_token' not in resp:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description'])
        return redirect(next_url)
    session['logged_in'] = True
    session['oauth_token'] = (resp['access_token'], '')
    
    return redirect(next_url)

@app.route("/logout")
def logout():
    pop_login_session()
    return redirect(url_for('about'))


@app.route('/profile')
def profile():
    me = facebook.get('/me')
    name = me.data['name']
    fname = me.data['first_name']
    lname = me.data['last_name']
    #uname = me.data['username']
    #gender - me.data['gender']
    id = me.data['id']
    email = me.data['email']
    return render_template('pages/profile.html',
                            user = fname,
                            name = name,
                            id = id,
                            email = email)


# Error handlers.

@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500

@app.errorhandler(404)
def internal_error(error):
    return render_template('errors/404.html'), 404




if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')
    


#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''

