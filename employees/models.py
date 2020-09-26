from sqlalchemy import Column, Integer, String, Unicode, Date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EmployeeDirectory(Base):
    __tablename__ = 'employee_directory'

    eid = Column(Integer, primary_key=True)
    name = Column(Unicode(255), nullable=False)
    gender = Column(String(1), nullable=False)
    hire_date = Column(Date, nullable=False)
    department = Column(Unicode(255), nullable=False)
    division = Column(Unicode(255), nullable=False)
    job_code = Column(Unicode(255), nullable=False)
    manager = Column(Unicode(255), nullable=False)
    performance = Column(Unicode(255), nullable=False)
    annual_benefits_value = Column(Unicode(255), nullable=False)