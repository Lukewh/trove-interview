Amazon Wage Portal


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
