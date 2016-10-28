from flask import Flask, request
import ultimate

app = Flask(__name__)

@app.route('/guitar-tabs/', methods=['GET'])
def display():
	query = request.args.get('query') or None
	if query:
		try:
			data = ultimate.getContents(ultimate.getBestLink(query))
			back = "<a href='/guitar-tabs/'>GO BACK</a>"
			return back + "<p> " + data.replace("\n", "<br>") + "</p>"
		except Exception:
			return "Song dosen't exist"
	else:
		return """
		<form method='GET' action="/guitar-tabs/">
			<input type='text' placeholder='search song' name='query'>
			<input type='submit' value='search'>
		</form>
		"""

if __name__ == '__main__':
    app.run()
