from flask import Flask, render_template, request
import pudb, random

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/tiny', methods=['POST'])
def tiny():
	url = request.form['url']
	num = random.randint(10000, 99999)


	return render_template('tinyURL.html', url=url)

if __name__ == '__main__':
	app.run(debug=True)