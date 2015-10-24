from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    ForeignKey,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

import datetime


# class MyModel(Base):
#     __tablename__ = 'models'
#     id = Column(Integer, primary_key=True)
#     name = Column(Text)
#     value = Column(Integer)

class Batch(Base):
    __tablename__ = 'batch'
    id = Column(Integer, primary_key=True)
    priority = Column(Integer, default=9001)
    project = Column(Text, default = "default")
    jira_ticket = Column(Text, default = "default")
    file_path = Column(Text, default = "default")
    pipeline = Column(Text, default = "default")
    active = Column(Text, default = "default")
    procedure = Column(Text, default = "default")
    progress = Column(Text, default = "default")
    running = Column(Integer, default = "default")
    failed = Column(Integer, default = "default")
    pending = Column(Text, default = "default")
    details = Column(Text, default = "default")
    log = Column(Text, default = "default")

class Queue(Base):
    __tablename__ = 'queue'
    id = Column(Integer, primary_key=True)
    analysis = Column(Text, default = "default")
    quota = Column(Integer, default=9001)
    running = Column(Text, default="default")
    waiting = Column(Text, default = "default")
    error = Column(Text, default = "default")
    identifier = Column(Text, default = "default")

class Merge(Base):
    __tablename__ = 'merge'
    id = Column(Integer, primary_key=True)
    library = Column(Text, default = "default")
    project = Column(Text, default = "default")
    num_alc = Column(Integer, default=9001)
    genome_ref = Column(Integer, default=9001)
    seq_len = Column(Integer, default=9001)
    success = Column(Text, default = "default")
    status = Column(Text, default = "default")
    data_path = Column(Text, default = "default")
    process_start = Column(Text, default = "default")
    process_complete = Column(Text, default = "default")



# Index('my_index', MyModel.name, unique=True, mysql_length=255)


