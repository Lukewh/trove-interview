from sqlalchemy import Column, Integer, String, Unicode, Date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class EmployeeDirectory(Base):
    __tablename__ = 'employee_directory'

    eid = Column(Integer, primary_key=True, index=True)
    name = Column(Unicode(255), nullable=False)
    gender = Column(String(1), nullable=False)
    hire_date = Column(Date, nullable=False)
    department = Column(Unicode(255), nullable=False)
    division = Column(Unicode(255), nullable=False)
    job_code = Column(Unicode(255), nullable=False)
    manager = Column(Unicode(255), nullable=False)
    performance = Column(Unicode(255), nullable=False)
    annual_benefits_value = Column(Unicode(255), nullable=False)


class SalaryHistory(Base):
    __tablename__ = 'salary_history'

    id  = Column(Integer, primary_key=True, autoincrement=True)
    eid = Column(Integer, nullable=False, index=True)
    salary = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)

    employee_directory = relationship("EmployeeDirectory", foreign_keys=[eid])