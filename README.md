```
sudo apt-get install python3-pip
pip3 install flask flask-wtf
sudo apt install python3-dev libpq-dev
pip3 install psycopg2 Flask-SQLAlchemy Flask-Migrate Flask-Script
pip3 install pylint-flask pylint-flask-sqlalchemy
```

Add this to .vscode/settings.json
```
"python.linting.pylintArgs": ["--load-plugins", "pylint-flask", "pylint-flask-sqlalchemy"
```