from app import app
from flask import Flask, render_template, redirect, session, request, flash, jsonify
import requests
import re
import os
from app.models.user import User
from flask_cors import CORS
CORS(app)


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    return render_template('dashboard.html', user=User.getOne(data))

@app.route('/superhero')
def superhero():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    return render_template('superhero.html', user=User.getOne(data))

@app.route('/search')
# @cross_origin()
def getData():
    print(request.form['query'])
    r = request.get(f"https://superheroapi.com/api/{os.environ.get('API_KEY')}/search/{request.form['query']}")
    print("print r: ", r)
    print("print json: ", r.json())
    return jsonify(r.json())

@app.route('/getTune', methods=['POST'])
def getTune():
    r = request.get(f"https://looney-toons-api.herokuapp.com/api/characters")
    print("print Tunes: ", r.json())
    return jsonify(r.json())