import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Secret key for session management. You can generate random strings here:

SECRET_KEY = '_M4v-kA_hx8q2-4Wshu6K-F-KXtJRG'
FACEBOOK_APP_ID = '188477911223606'
FACEBOOK_APP_SECRET = '621413ddea2bcc5b2e83d42fc40495de'


# Connect to the database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
# Database migration folder
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
