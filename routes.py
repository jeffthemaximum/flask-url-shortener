from flask import Flask, render_template, request, redirect
import pudb, random
from random import shuffle
import models
import json

app = Flask(__name__)
my_dict = {}

def key_generator(url):
	short = []
	for i in range(0,2):
		upper = random.randint(65, 90)
		short.append(str(unichr(int(upper))))
		lower = random.randint(97, 122)
		short.append(str(unichr(int(lower))))
		num = random.randint(10, 99)
		short.append(str(num))
	shuffle(short)
	new_url = "".join(short)
	return new_url

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/tiny', methods=['POST'])
def tiny():
	#get url from html form
	url = request.form['url']

	#generate short url key
	new_url = key_generator(url)

	#insert url, key, hitcount into sqlite3 db
	models.insert_link(new_url, url, 0)

	#query hitcount from db
	hits = models.query_hits_and_url_for_link(new_url)[0][3]

	#render tinyURL.html with url, new_url, and hits params
	return render_template('tinyURL.html', url=url, new_url=new_url, hits=hits)

@app.route('/<key>', methods=['GET'])
def redirect_tiny(key):
	try:
		url = models.query_hits_and_url_for_link(key)[0][2]
	except:
		url = ""
	long_url = 'http://' + url
	models.update_hits(key)
	return redirect(long_url, code=302)

@app.route('/getmethod/<key>')
def get_js_data(key):
	return "hello, world!"

if __name__ == '__main__':
	app.run(debug=True)