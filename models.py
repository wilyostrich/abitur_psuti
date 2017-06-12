from sqlalchemy import Column, Integer, Unicode
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Academic(Base):
    __tablename__ = 'academic_bachelor'
    id_spec = Column(Integer, primary_key=True)
    name = Column(Unicode(length=200))
    prof_link = Column(Unicode(length=200))
    examinations = Column(Unicode(length=200))
    budgetary_place = Column(Unicode(length=200))
    contract_places = Column(Integer)
    cost = Column(Unicode(length=100))

    def __str__(self):
        return '<Specialty: {}, {}>'.format(self.name, self.examinations)

    def __repr__(self):
        return '<Specialty: {}, {}>'.format(self.name, self.examinations)


class Applied(Base):
    __tablename__ = 'applied_bachelor'
    id_spec = Column(Integer, primary_key=True)
    name = Column(Unicode(length=200))
    prof_link = Column(Unicode(length=200))
    examinations = Column(Unicode(length=200))
    budgetary_place = Column(Unicode(length=200))
    contract_places = Column(Integer)
    cost = Column(Unicode(length=100))

    def __str__(self):
        return '<Specialty: {}, {}>'.format(self.name, self.examinations)

    def __repr__(self):
        return '<Specialty: {}, {}>'.format(self.name, self.examinations)


class Specialty(Base):
    __tablename__ = 'specialty'
    id_spec = Column(Integer, primary_key=True)
    name = Column(Unicode(length=200))
    prof_link = Column(Unicode(length=200))
    examinations = Column(Unicode(length=200))
    budgetary_place = Column(Unicode(length=200))
    contract_places = Column(Integer)
    cost = Column(Unicode(length=100))

    def __str__(self):
        return '<Specialty: {}, {}>'.format(self.name, self.examinations)

    def __repr__(self):
        return '<Specialty: {}, {}>'.format(self.name, self.examinations)
