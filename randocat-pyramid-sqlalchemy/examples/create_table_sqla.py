# catdb.py

from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:', echo=True)

metadata = MetaData()
users = Table('cat', metadata,
     Column('id', Integer, primary_key=True),
     Column('url', String),
)

if __name__=='__main__':
	metadata.create_all(engine)