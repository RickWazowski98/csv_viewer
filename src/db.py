from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

db_path = os.path.abspath('table.db')
engine = create_engine(f'sqlite:///{db_path}', echo=True)
Session = sessionmaker(bind=engine)
session = Session()