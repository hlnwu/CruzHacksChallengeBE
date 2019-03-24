#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# template from CruzHacks 2019

from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os
        
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# hacker model
class Hacker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False)
    age = db.Column(db.Integer, unique=False)
    school = db.Column(db.String(64), unique=False)
    major = db.Column(db.String(64), unique=False)
    email = db.Column(db.String(64), unique=False)
    phone = db.Column(db.String(32), unique=True)
    physicalAccommodations = db.Column(db.Boolean, unique=False)
    dietaryAccommodations = db.Column(db.Boolean, unique=False)
    isCheckedIn = db.Column(db.Boolean, unique=False)

    def __init__(self, name, age, school, major, email, phone, \
            physicalAccommodations, dietaryAccommodations, isCheckedIn):
        self.name = name
        self.age = age
        self.school = school
        self.major = major
        self.email = email
        self.phone = phone
        self.physicalAccommodations = physicalAccommodations
        self.dietaryAccommodations = dietaryAccommodations
        self.isCheckedIn = isCheckedIn
      
# hacker schema
class HackerSchema(ma.Schema):
    class Meta:
        fields = ('name', 'age', 'school', 'major', 'email', 'phone', \
                'physicalAccommodations', 'dietaryAccommodations', 'isCheckedIn')

hacker_schema = HackerSchema()
hackers_schema = HackerSchema(many=True)

# main page with no info on it
@app.route("/")
def main_page():
    return ""

# endpoint 
@app.route("/hackers", methods=["POST"])

def add_hacker():
    name = request.json['name']
    age = request.json['age']
    school = request.json['school']
    major = request.json['major']
    email = request.json['email']
    phone = request.json['phone']
    physicalAccommodations = request.json['physicalAccommodations']
    dietaryAccommodations = request.json['dietaryAccommodations']
    isCheckedIn = request.json['isCheckedIn']
    
    new_hacker = Hacker(name, age, school, major, email, phone, \
            physicalAccommodations, dietaryAccommodations, isCheckedIn)
        
    db.session.add(new_hacker)
    db.session.commit()
    return str(new_hacker)


# endpoint to show all hackers
@app.route("/hackers", methods=["GET"])
def get_hacker():
    all_hackers = Hacker.query.all()
    result = hackers_schema.dump(all_hackers)
    return jsonify(result.data)

# endpoint to get hacker detail by id
@app.route("/hackers/<id>", methods=["GET"])
def hacker_detail(id):
    hacker = Hacker.query.get(id)
    return hacker_schema.jsonify(hacker)

# endpoint to update hacker
@app.route("/hackers/<id>", methods=["PUT"])
def hacker_update(id):
    hacker = Hacker.query.get(id)
    hacker.name = request.json['name']
    hacker.age = request.json['age']
    hacker.school = request.json['school']
    hacker.major = request.json['major']
    hacker.email = request.json['email']
    hacker.phone = request.json['phone']
    hacker.physicalAccommodations = request.json['physicalAccommodations']
    hacker.physicalAccommodations = request.json['dietaryAccommodations']
    hacker.isCheckedIn = request.json['isCheckedIn']

    db.session.commit()
    return hacker_schema.jsonify(hacker)

# endpoint to delete hacker
@app.route("/hackers/<id>", methods=["DELETE"])
def hacker_delete(id):
    hacker = Hacker.query.get(id)
    db.session.delete(hacker)
    db.session.commit()

    return hacker_schema.jsonify(hacker)



if __name__ == '__main__':
    app.run(debug=True) 
