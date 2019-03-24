# CruzHacksChallengeBE

## Setting Up Flask
Before starting anything, make sure to have the 3rd party tool "virtualenv" installed.

After cloning the repository, create a virtual environment using:
```
$ virtualenv venv
```
Once everything is done installing, run the virtual environment:
```
$ source venv/bin/activate
```
If you are using Windows, use this command to run the virtual environment:
```
$ venv/Scripts/activate
```
When your virtual environment starts up, install Flask and SQLAlchemy:
```
$ pip install flask
$ pip install flask_sqlalchemy
$ pip install marshmallow-sqlalchemy
```

## Setting Up the Database
Run `python`.
In Python, run 
```
>>> from app import db
>>> db.create_all()
```
to create the database.
Now you can run `python app.py` to start the Flask application!

## Note
If you ever want to see all the hackers you've inputted, go to:
```
http://127.0.0.1:5000/hackers
```
