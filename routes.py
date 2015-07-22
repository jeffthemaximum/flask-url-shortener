from flask import Flask, render_template, request, redirect
import pudb, random
from random import shuffle
import models

app = Flask(__name__)
my_dict = {}

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/tiny', methods=['POST'])
def tiny():
	url = request.form['url']
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
	my_dict[new_url] = url
	models.insert_link(new_url, url, 0)

	return render_template('tinyURL.html', url=url, new_url=new_url)

@app.route('/<key>', methods=['GET'])
def redirect_tiny(key):
	long_url = 'http://' + my_dict[key]
	models.update_hits(key)
	models.query_hits_for_link(key)
	return redirect(long_url, code=302)

if __name__ == '__main__':
	app.run(debug=True)