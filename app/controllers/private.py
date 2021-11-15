from app import app
from flask import Flask, render_template, redirect, session, request, flash
import re
from  flask_bcrypt import Bcrypt
from app.models.user import User


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    return render_template('dashboard.html', user=User.getOne(data))