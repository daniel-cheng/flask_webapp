import os, json, urllib2
from flask import Flask, render_template
 
 # Create Flask instance using current shell name (this allows running on both your computer and on a server)
app = Flask(__name__)

# .route Decorator function creates the actual URL structure of the site - see example below for adding additional pages
@app.route('/')
@app.route('/home')
def hello_world():
	# print("HTML Accessed")
	#Flask utilizes Jinja2 to dynamically parse html files. render_template bascially returns a string of the html file, but with subsituted information from Jinja2.
	url = "https://www.googleapis.com/youtube/v3/videos?id=7lCDEYXw3mM&key=AIzaSyCvmUuH7_MNaGQG5Sxbb6jhyVTa_5aLCA8&part=snippet,contentDetails,statistics,status"
	data = json.load(urllib2.urlopen(url))
	viewCount = data['items'][0]['statistics']['viewCount']
	thumbnail = data['items'][0]['snippet']['thumbnails']['medium']['url']
	return render_template('home.html', viewCount=viewCount, dummy="dummy", thumbnail=thumbnail)
 
# Example of adding pages. Uncomment for fun.
# @app.route('/stylesheet')
# def stylesheet():
    # with open("static\stylesheets\stylesheet.css", "r") as css:
        # css_string = css.read()
	# print("CSS Accessed")
    # return css_string    
	
if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True)
 
