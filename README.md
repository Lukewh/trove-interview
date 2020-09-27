Amazon Wage Portal
==========
![splash](https://github.com/theleastinterestingcoder/trove-interview/blob/master/screenshot-splash.png)

Architecture
-----------
![diagram](https://github.com/theleastinterestingcoder/trove-interview/blob/master/diagram.png)

## Overview and Approach

This is a basic three tiered app hosted mostly in EC2. Ideally, I would have used [JAM-stack](https://jamstack.org/) or serverless, but since I'm interviewing for a backend/infra position, I decided to try to demonstrate both bits by unbundling a serverless stack

This involves a lot overhead setting things up (I now appreciate Firebaise/Heroku/serverless more), which ate away a lot of my time but hopefully demonstrates the understanding of the fundamental components. 

Decisions and forward architecture:
* **DNS + service resolution** - I used namecheap pointing the "A" record to an Elastic IP since this is simple. This can be extended to Route 53 if we wanted a unified API layer while supporting a duo server/serverless architecture. 
* **Middle layer and app** - I chose flask w/ python3 for simplicity over django for serving requests. The rest is pretty standard python: SQL alchemy as my ORM and alembic for data/schema migrations.
* **Persistence** - MySQL RDMS for simplicity (I also know this like the back of my hand)*

(*) Note: I actually wanted to pick redshift/snowflake/bigquery since these database engines are columnar stores, which are highly efficient for analyzing business data at scale. Then we don't have to spend time on optimizing queries (e.g. constructing indexes, etc).

What I would work on next given then time:
- Write more business logic to grab and visualize data more efficiently
- Figure out how chart.js would work so I visualize analysis (e.g. box and whisker plot)
- Spruce up code deployment
- Use docker/kubernetes


Setting up the virtual environment:
------
```
python3 -m venv .venv
source ./.venv/bin/activate
pip3 install -r requirements.txt
python app.py
```

Setting up the server:
-----
```
sudo apt-get install mysql-server
sudo apt-get install libmysqlclient-dev
sudo apt-get install libpq-dev
sudo apt-get install build-essential
````

For Production:
------
```
export PROD_CONNECTION_STRING="mysql://{{username}}:{{password}}@trove-interview-2.coqr8ui6dees.us-west-1.rds.amazonaws.com:3306/trove"
```
