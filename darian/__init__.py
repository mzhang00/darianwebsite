from flask import Flask, render_template, request, session, redirect, url_for, flash, jsonify
import os
import urllib, json, sqlite3
from json import loads

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('website.html')

if __name__ == "__main__":
    DIR = os.path.dirname(__file__)
    DIR += '/'
    app.debug = True
    app.run(host='0.0.0.0')
