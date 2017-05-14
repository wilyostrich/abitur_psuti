from models import Base
from sqlalchemy import create_engine


engine = create_engine("postgresql://postgres:1234@localhost/abitur")
Base.metadata.create_all(engine)