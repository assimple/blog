from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

eng = create_engine('postgresql://postdb:123456@localhost/test')
Base = declarative_base()
Base.metadata.bind = eng
