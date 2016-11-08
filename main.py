from flask import Flask, request, render_template
import ultimate
from twitter import Twitter

app = Flask(__name__)

def filterText(text):
	clean_text = ""
	allowed = """qwertyuiopasdfghjklzxcvbnm ,.-/\\\"\'?
	QWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()-+=_`~<>;:|[]}{"""
	for letter in text:
		if letter in allowed:
			clean_text += letter
	return clean_text

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/guitar-tabs/', methods=['GET'])
def display():
	query = request.args.get('query') or None
	if query:
		try:
			data = ultimate.getContents(ultimate.getBestLink(query))
			button = '''<a href="/guitar-tabs/"><button class="btn btn-primary">GO BACK</button></a><br><br>'''
			tab = button + data.replace("\n", " <br> ")
			html_code = open('templates/frame.html').read()
			file = open('templates/tabs1.html', 'w')
			file.write(html_code.replace("~~~CUE~~~", tab))
			file.close()
			return render_template('tabs1.html')
		except Exception as e:
			return "<br><br>" + "Couldn't find the song..." + str(e)
	else:
		return render_template('search.html')

@app.route('/twitter-api/', methods=['GET'])
def twitter():
	tObj = Twitter()

	tag = request.args.get('tag') or None
	if tag:
		try:
			tweets = tObj.getTweets(tag)
			display = ""
			for tweet in tweets:
				display += filterText(tweet.text) + "<br><br>"
			html_code = open('templates/frame.html').read()
			file = open('templates/tweets.html', 'w')
			file.write(html_code.replace("~~~CUE~~~", display))
			file.close()
			return render_template('tweets.html')
		except Exception as e:
			return "<br><br><p class='lead'>ERROR 111</p><br><br>Something went wrong.." + str(e)
	else:
		return render_template("twitter_home.html")		

if __name__ == '__main__':
    app.run(port=8000)
