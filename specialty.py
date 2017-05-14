from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData

engine = create_engine("postgresql://postgres:1234@localhost/abitur")

