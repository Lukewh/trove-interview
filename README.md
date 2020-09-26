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

Useful Links:
-------
* https://u.osu.edu/walujo.1/2016/07/07/associate-namecheap-domain-to-amazon-ec2-instance/
* https://ubuntu.com/tutorials/install-and-configure-apache#2-installing-apache
* https://medium.com/@prithvishetty/deploying-a-python-3-flask-app-into-aws-using-apache2-wsgi-1b26ed29c6c2
* https://certbot.eff.org/lets-encrypt/ubuntufocal-apache
* https://www.youtube.com/watch?v=Ng_zi11N4_c&t=148s&ab_channel=BeABetterDev
