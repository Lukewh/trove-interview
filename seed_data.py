"""
Process Directory information
"""

import csv
from employees.models import EmployeeDirectory, SalaryHistory
from collections import OrderedDict
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine(os.environ['PROD_CONNECTION_STRING'])
conn = engine.connect()
session_maker = sessionmaker(bind=engine)
session = session_maker()

employee_directory_source="data/2020-09-26_employee_directory_data.csv"
salary_table_source = "data/2020-09-26_salary_data.csv"

# Clear tables
session.query(EmployeeDirectory).delete()
session.query(SalaryHistory).delete()

# Upload employee data
with open(employee_directory_source, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        entry = EmployeeDirectory(**row)
        session.add(entry)

# Upload salary data
with open(salary_table_source, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        entry = SalaryHistory(**row)
        session.add(entry)

session.commit()


