import os
from flask import Flask, render_template
 
 # Create Flask instance using current shell name (this allows running on both your computer and on a server)
app = Flask(__name__)

# .route Decorator function creates the actual URL structure of the site - see example below for adding additional pages
@app.route('/')
@app.route('/home')
def hello_world():
	# print("HTML Accessed")
	#Flask utilizes Jinja2 to dynamically parse html files. render_template bascially returns a string of the html file, but with subsituted information from Jinja2.
	return render_template('home.html')
 
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
	app.run(host='0.0.0.0', port=port)
 
