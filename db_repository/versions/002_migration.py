from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
friend = Table('friend', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', Integer),
    Column('email', Integer),
    Column('dob', DateTime),
    Column('country', Integer),
    Column('lastmessage', Integer),
    Column('user_id', Integer),
)

user = Table('user', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', Integer),
    Column('email', Integer),
    Column('configkey', Integer),
    Column('dob', DateTime),
    Column('country', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['friend'].drop()
    pre_meta.tables['user'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['friend'].create()
    pre_meta.tables['user'].create()
