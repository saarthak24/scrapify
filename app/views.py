from app import app
from flask import send_file
from flask import render_template, redirect, jsonify

def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
@app.route('/downloads')
def get_downloads():
	return app.send_static_file('download.html')
@app.route('/download')
def return_files_tut():
    res = {'download' : 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'}
    return jsonify(res)
