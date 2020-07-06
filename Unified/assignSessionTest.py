# from assignSchema import * ## this is the old afs-sqlite based database
# , LogRecord, Lock
from assignSchemaTest import Base, Workflow, Output, Transfer, engine, TransferImp
from sqlalchemy.orm import sessionmaker
import time
import copy
import random

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
