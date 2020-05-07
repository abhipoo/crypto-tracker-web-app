from flask import Flask, jsonify
import aws_controller

app = Flask(__name__)

@app.route('/')
def index():
	return "Main page"

@app.route('/crypto')
def crypto():
	#return "Crypto rates"
	return jsonify(aws_controller.get_items())