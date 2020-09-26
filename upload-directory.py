"""
Process Directory information
"""

import csv
from employees.models import EmployeeDirectory
from collections import OrderedDict
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine(os.environ['PROD_CONNECTION_STRING'])
conn = engine.connect()
session_maker = sessionmaker(bind=engine)
session = session_maker()

source="/Users/quanzhou/Downloads/2020-09-26_trove-employee-directory.csv"

with open(source, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        entry = EmployeeDirectory(**row)
        session.add(entry)

session.commit()