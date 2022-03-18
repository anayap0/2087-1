from flask import render_template
from app import app

@app.route('/')
def page():
    return render_template('chart.html')
