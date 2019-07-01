import os

from flask import (
    Flask,
    request,
    jsonify,
    send_from_directory,
    render_template,
    redirect,
    url_for,
)
from main import app
from auto_makeanswer import auto_makeanswer

@app.route('/') #route、つまりTOPページ？にアクセスがあった途端に実行すること
def index():
  return render_template('index.html')

@app.route('/generate', methods=['GET'])
def generate():
  return render_template('index.html', **{
    'coef': auto_makeanswer()
    })