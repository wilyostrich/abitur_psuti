from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData
from sqlalchemy import orm


engine = create_engine("postgresql://postgres:1234@localhost/abitur")
meta = MetaData(bind=engine, reflect=True)

class Rating(object):
    pass
orm.Mapper(Rating, meta.tables['specialties'])
s = orm.Session(bind=engine)
s.query(Rating).filter(Rating.id_spec == 1).count()
print(s.query(Rating).filter(Rating.id_spec == 1))



