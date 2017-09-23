from app import app
from flask import send_file
from flask import render_template, redirect, jsonify, request
from .utility import parser

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
    url = request.args.get("show_url")
    ep = request.args.get("episode")
    vid_url = parser.get_vid_url(url,ep)
    res = {'download' : str(vid_url)}
    return jsonify(res)
