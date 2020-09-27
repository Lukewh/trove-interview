from flask import Flask, render_template
from flask import jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

app = Flask(__name__, static_url_path='', static_folder='static')

engine = create_engine(os.environ['PROD_CONNECTION_STRING'])
conn = engine.connect()
session_maker = sessionmaker(bind=engine)
session = session_maker()

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/analysis')
def get_analysis():
    data = get_salary_data()
    return jsonify(data)

def get_salary_data():
    raw_data = conn.execute(
        '''
        select ed.eid, ed.gender, ed.name, sh.salary, ed.division, sh.date
        from employee_directory ed inner join salary_history sh on ed.eid = sh.eid
        group by ed.eid, ed.name, sh.salary, ed.division, sh.date order by sh.date desc
        limit 100;
        '''
    )

    by_division = {}

    for eid, gender, name, salary, division, date  in raw_data:
        value = by_division.get(division, [])
        value.append(salary)

        by_division[division] = value

    flattened = [(k, *v) for k,v in by_division.items()]
    return flattened


if __name__ == "__main__":
    app.run()
