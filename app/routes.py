from flask import render_template, request, abort
from app import app

SECRET_KEY = 'hackedbyz!'

@app.route('/')
def index():
    key = request.args.get('key')
    if key == SECRET_KEY:
        return render_template('index.html')
    else:
        abort(403)
